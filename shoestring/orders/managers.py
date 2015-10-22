from django.db import models


class OrderItemQuerySet(models.QuerySet):

    def with_total(self):
        return self.annotate(total=models.F('price') * models.F('quantity'))
