import os.path
from urllib.parse import unquote

from django import http
from django.db.models import Count
from django.contrib.postgres.search import SearchQuery, SearchVector

from easy_thumbnails.alias import aliases
from easy_thumbnails.exceptions import EasyThumbnailsError
from easy_thumbnails.files import get_thumbnailer

from nap.rest import views

from ..utils import Patterns

from . import mappers, models

urlpatterns = Patterns()


class ProductMixin:
    model = models.Product
    mapper_class = mappers.ProductMapper

    def get_queryset(self):
        return super().get_queryset().enabled()


# Allowable ordering field map
ORDER_MAP = {
    'price': 'price',
    'name': 'name',
}
DIRECTION_MAP = {
    'desc': '-',
}


@urlpatterns(r'^$', name='product-list')
class ProductListView(ProductMixin,
                      views.ListGetMixin,
                      views.BaseListView):

    def get_queryset(self):
        qset = super().get_queryset()
        # Apply search
        q = self.request.GET.get('q')
        if q:
            qset = qset.annotate(
                search=SearchVector('sku', 'name', 'description', 'brand__name')
            ).filter(
                search=SearchQuery(q)
            )
        # Apply filters
        tags = self.request.GET.getlist('tag')
        if tags:
            qset = qset.filter(tags__contains=tags)
        brands = self.request.GET.getlist('brand')
        if brands:
            qset = qset.filter(brand__name__in=brands)
        # Apply sorting
        order = ORDER_MAP.get(self.request.GET.get('order', 'price'))
        if order:
            direction = DIRECTION_MAP.get(self.request.GET.get('dir'), '')
            qset = qset.order_by(direction + order)
        return qset

    def get(self, request):
        '''
        Produce a combined set of data:
        {
            tags: [
                {name, count, total, active},
            ],
            brands: [
                {name, count, total, active},
            ],
            products: [...],
        }
        '''
        qset = self.get_queryset()

        selected_tags = self.request.GET.getlist('tag')
        totals = dict(models.Product.objects.count_tag_values('tags'))
        counts = dict(qset.count_tag_values('tags'))
        tags = [
            {
                'name': tag,
                'active': tag in selected_tags,
                'total': totals[tag],
                'count': counts.get(tag, 0),
            }
            for tag in sorted(totals)
        ]

        selected_brands = self.request.GET.getlist('brand')
        totals = models.Brand.objects.annotate(total=Count('product'))
        counts = dict(models.Brand.objects.filter(product__in=qset).values_list('name').annotate(Count('name')))
        brands = [
            {
                'name': brand.name,
                'active': brand.name in selected_brands,
                'total': brand.total,
                'count': counts.get(brand.name, 0),
            }
            for brand in totals
        ]
        self.mapper = self.get_mapper()
        return http.JsonResponse({
            'tags': tags,
            'brands': brands,
            'products': [
                self.mapper << obj
                for obj in qset
            ]
        })


@urlpatterns(r'^(?P<alias>[\w-]+)/(?P<path>.*)$', name='thumbnail')
def thumbnail(request, alias, path):
    '''Redirect to a thumbnail as configured with GET params'''

    # Clean up path
    path = os.path.normpath(path)
    # Unescape
    path = unquote(path)

    options = aliases.get(alias)

    # Create thumbnail
    try:
        thumbnail = get_thumbnailer(path).get_thumbnail(options)

        return http.HttpResponsePermanentRedirect(thumbnail.url)

    except EasyThumbnailsError:
        raise http.Http404
