from nap import mapper
from nap.utils.ripper import Ripper

from . import models

ItemRipper = Ripper('sku', 'name', 'description', 'quantity', 'price', 'status', name='brand.name')


class OrderMapper(mapper.ModelMapper):
    class Meta:
        model = models.Order
        exclude = ('user',)

    @mapper.field
    def items(self):
        return [
            ItemRipper(item)
            for item in self.items.all()
        ]
