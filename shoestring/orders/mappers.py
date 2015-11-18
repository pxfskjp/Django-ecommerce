from nap.datamapper import ModelDataMapper, field
from nap.utils.ripper import Ripper

from . import models

ItemRipper = Ripper('sku', 'name', 'description', 'quantity', 'price', 'status', name='brand.name')


class OrderMapper(ModelDataMapper):
    class Meta:
        model = models.Order
        exclude = ('user',)

    @field
    def items(self):
        return [
            ItemRipper(item)
            for item in self.items.all()
        ]
