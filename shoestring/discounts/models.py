from django.db import models
# 1.9
# from django.db.models.functions import Now
from django.utils import timezone

from array_tags.fields import TagField


class BaseDiscount(models.Model):
    description = models.CharField(max_length=1000)

    valid_from = models.DateTime(default=timezone.now)
    valid_until = models.DateTimeField(blank=True, null=True)

    outcome = models.ForeignKey('Outcome')

    class Meta:
        abstract = True


class ProductDiscountQuerySet(models.QuerySet):

    def current(self):
        return self.filter(
            Q(valid_until__gt=now)|Q(valid_until=None),
            valid_from__lte=now,
        )

    def for_product(self, product):
        now = timezone.now()
        self.filter(
            include_tags__unnest__in=product.tags,
            include_brand=product.brand,
        ).exclude(
            exclude_tags__unnest__in=product.tags,
            exclude_brand=product.brand,
        )


class ProductDiscount(BaseDiscount):

    include_tags = TagField(blank=True)
    exclude_tags = TagField(blank=True)

    include_brands = models.ManyToManyField('products.Brand')
    exclude_brands = models.ManyToManyField('products.Brand')

    objects = ProductDiscountQuerySet.as_manager()


class CartDiscount(BaseDiscount):
    pass

class Rule(models.Model):
    discount = models.ForeignKey('CartDiscount')
    mode = models.BooleanField(choices=(
        (False, 'Exclude'),
        (True, 'Include'),
    ))
    condition = models.ForeignKey('Condition')
