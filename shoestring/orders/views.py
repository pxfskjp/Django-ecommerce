
from nap import http
from nap.rest import views

from . import mappers
from . import models

from ..cart.cart import Cart


class OrderMixin:
    model = models.Order
    mapper_class = mappers.OrderMapper


class OrderListView(OrderMixin,
                    views.ListGetMixin,
                    views.BaseListView):

    def post(self, request):
        cart = Cart.from_session(self.request.session)
        if not cart:
            return http.BadRequest()
        order = models.Order.from_cart(request.user, cart)
        return http.OK()
