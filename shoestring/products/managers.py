from array_tags.managers import TagQuerySet


class ProductQuerySet(TagQuerySet):

    def enabled(self):
        return self.filter(enabled=True)
