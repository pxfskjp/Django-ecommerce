from nap.rest import views

from . import mappers
from . import models


class ProductMixin:
    model = models.Product
    mapper_class = mappers.ProductMapper

    def get_queryset(self):
        return super().get_queryset().enabled()


class ProductListView(ProductMixin,
                      views.ListGetMixin,
                      views.BaseListView):
    pass
