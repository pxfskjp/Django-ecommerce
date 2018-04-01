from django.contrib.auth.mixins import LoginRequiredMixin

from nap import http
from nap.rest import views

from . import mappers, models
from ..cart.cart import Cart
from ..payments.models import Payment


class OrderMixin:
    model = models.Order
    mapper_class = mappers.OrderMapper


class OrderListView(OrderMixin,
                    LoginRequiredMixin,
                    views.ListGetMixin,
                    views.BaseListView):

    def post(self, request):
        cart = Cart.from_session(self.request.session)
        if not cart:
            return http.BadRequest()
        order = models.Order.from_cart(request.user, cart)
        request.session['order_id'] = order.pk
        return self.get(request)

    def delete(self, request):
        order = get_object_or_404(
            models.Order,
            user=self.request.user,
            pk=request.session.get('order_id')
        )
        if order.payment_set.filter(state=Payment.STATE.APPROVED).exists():
            # Can't delete an order with a payment
            return http.Conflict()

        order.delete()
        request.session.pop('order_id')
        return http.NoContent()
