from nap.datamapper import ModelDataMapper, field
from taggit.models import Tag

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
    def tags(self):
        return list(self.tags.values('name', 'slug'))

    @field
    def images(self):
        return [
            i.image.name
            for i in self.images.all()
        ]


class TagMapper(ModelDataMapper):
    class Meta:
        model = Tag
        fields = '__all__'

    @field
    def count(self):
        return self.num_times
