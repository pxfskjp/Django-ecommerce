from nap.datamapper import DataMapper, Field, field


class CartItemMapper(DataMapper):
    sku = Field('sku')
    qty = Field('qty')

    @field
    def name(self):
        return self.product.name

    @field
    def price(self):
        return float(self.product.price)
