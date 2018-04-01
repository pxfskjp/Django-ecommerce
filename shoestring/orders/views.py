from django.contrib.auth.mixins import LoginRequiredMixin

from nap import http
from nap.rest import views
from nap.shortcuts import get_object_or_404

from . import mappers, models
from ..cart.cart import Cart
from ..payments.models import Payment
from ..utils import Patterns


urlpatterns = Patterns()


class OrderMixin:
    model = models.Order
    mapper_class = mappers.OrderMapper


@urlpatterns(r'^$', name='checkout')
class CheckoutView(OrderMixin,
                   views.ObjectGetMixin,
                   views.BaseObjectView):

    def get_object(self, queryset=None):
        obj_id = self.request.session.get('order_id')
        return self.model.objects.get(obj_id)

    def post(self, request):
        # If there's an existing order, cancel its items
        order_id = request.session.get('order_id')
        if order_id:
            models.OrderItem.object.filter(
                order__pk=order_id
            ).update(
                status=models.OrderItem.STATE.CANCELLED
            )

        cart = Cart.from_session(self.request.session)
        if not cart:
            return http.BadRequest()

        order = models.Order.from_cart(request.user, cart)
        request.session['order_id'] = order.pk
        return self.single_response(request, object=order)

    def delete(self, request):
        order = get_object_or_404(
            models.Order,
            pk=request.session.get('order_id')
        )
        if order.payment_set.filter(state=Payment.STATE.APPROVED).exists():
            # Can't delete an order with a payment
            return http.Conflict()

        order.delete()
        request.session.pop('order_id')
        return http.NoContent()
