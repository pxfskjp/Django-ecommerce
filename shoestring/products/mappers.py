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


class TagMapper(ModelDataMapper):
    class Meta:
        model = Tag
        fields = '__all__'

    @field
    def num_times(self):
        return self.num_times
