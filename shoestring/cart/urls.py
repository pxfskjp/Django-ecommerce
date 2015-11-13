from django.conf.urls import url

from . import views

urlpatterns = [
    url('^$',
        views.CartView.as_view(),
        name='cart'),
]
