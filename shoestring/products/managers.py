from django.db import models


class ProductQuerySet(models.QuerySet):

    def enabled(self):
        return self.filter(enabled=True)
