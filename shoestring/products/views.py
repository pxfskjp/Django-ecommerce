from nap.rest import views

from . import mappers, models


class ProductMixin:
    model = models.Product
    mapper_class = mappers.ProductMapper

    def get_queryset(self):
        return super().get_queryset().enabled()


class ProductListView(ProductMixin,
                      views.ListGetMixin,
                      views.BaseListView):
    pass


class TagListView(views.ListGetMixin,
                  views.BaseListView):
    mapper_class = mappers.TagMapper
    def get_queryset(self):
        return models.Product.tags.most_common()
