from nap.datamapper import ModelDataMapper, field

from . import models


class ProductMapper(ModelDataMapper):
    class Meta:
        model = models.Product
        fields = '__all__'
        exclude = ('enabled',)

    @field
    def brand(self):
        return self.brand.name

    @field
    def images(self):
        return [
            i.image.name
            for i in self.images.all()
        ]
