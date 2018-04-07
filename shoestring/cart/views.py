from django.utils.functional import cached_property

from nap import http, rpc

from ..utils import Patterns

from .cart import Cart
from .mappers import CartItemMapper


urlpatterns = Patterns()


@urlpatterns(r'^$', name='cart')
class CartView(rpc.RPCView):

    def get(self, request):
        return http.JsonResponse(self._render())

    @cached_property
    def cart(self):
        return Cart.from_session(self.request.session)

    def save(self):
        self.cart.save(self.request.session)

    def _render(self):
        '''Render the cart'''
        mapper = CartItemMapper()
        return {
            'total': float(self.cart.total()),
            'items': [
                mapper << item
                for item in self.cart.values()
            ],
        }

    @rpc.method
    def content(self):
        return self._render()

    @rpc.method
    def add(self, sku, quantity):
        '''
        Add an Item to the cart
        '''
        self.cart.add(sku, quantity)
        self.save()
        return self._render()

    @rpc.method
    def quantity(self, sku, quantity):
        '''
        Update quantity
        '''
        if quantity == 0:
            self.cart.pop(sku, None)
            self.save()
        else:
            try:
                self.cart[sku].quantity = quantity
                self.save()
            except KeyError:
                raise ValueError('Item not in cart', sku)

        return self._render()

    @rpc.method
    def clear(self):
        '''
        Clear the cart.
        '''
        self.request.session.pop('cart')
        self.save()
        return self._render()
