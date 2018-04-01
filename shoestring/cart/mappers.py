from nap import mapper


class CartItemMapper(mapper.Mapper):
    sku = mapper.Field('sku')
    quantity = mapper.Field('quantity')

    @mapper.field
    def name(self):
        return self.product.name

    @mapper.field
    def price(self):
        return float(self.product.price)
