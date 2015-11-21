import os.path
from urllib.parse import unquote

from easy_thumbnails.alias import aliases
from easy_thumbnails.exceptions import EasyThumbnailsError
from easy_thumbnails.files import get_thumbnailer
from nap.rest import views

from django import http

from . import mappers, models


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

class ProductListView(ProductMixin,
                      views.ListGetMixin,
                      views.BaseListView):

    def get_queryset(self):
        qset = super(ProductListView, self).get_queryset()
        # Apply filters
        for tag in self.request.GET.getlist('tag'):
            qset = qset.filter(tags__slug=tag)
        # Apply sorting
        order = ORDER_MAP.get(self.request.GET.get('order'))
        if order:
            direction = DIRECTION_MAP.get(self.request.GET.get('dir'), '')
            qset = qset.order_by(direction + order)
        return qset


class TagListView(views.ListGetMixin,
                  views.BaseListView):
    mapper_class = mappers.TagMapper

    def get_queryset(self):
        return models.Product.tags.most_common()


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
