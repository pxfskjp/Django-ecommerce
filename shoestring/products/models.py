from django.db import models

from array_tags.fields import TagField

from . import managers


class Brand(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class BaseProduct(models.Model):
    sku = models.SlugField(unique=True)
    name = models.CharField(max_length=200)
    brand = models.ForeignKey('products.Brand')
    description = models.TextField(blank=True)

    price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        abstract = True


class Product(BaseProduct):
    enabled = models.BooleanField(default=False, db_index=True)

    tags = TagField()

    objects = managers.ProductQuerySet.as_manager()


class Image(models.Model):
    product = models.ForeignKey('Product', related_name='images')
    image = models.ImageField(upload_to='products/')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('order',)
