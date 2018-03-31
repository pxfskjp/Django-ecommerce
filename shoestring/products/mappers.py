from nap import mapper
from . import models


class ProductMapper(mapper.ModelMapper):
    class Meta:
        model = models.Product
        fields = '__all__'
        exclude = ('enabled',)

    @mapper.field
    def brand(self):
        return self.brand.name

    @mapper.field
    def images(self):
        return [
            i.image.name
            for i in self.images.all()
        ]
