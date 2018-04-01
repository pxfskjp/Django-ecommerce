from django.conf import settings
from django.conf.urls import include, url
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie


urlpatterns = [
    url(r'^$',
        ensure_csrf_cookie(render),
        {
            'template_name': 'shoestring/index.html',
            'context': {'MEDIA_URL': settings.MEDIA_URL},
        },
        name='index'),
    url(r'^cart/',
        include(('shoestring.cart.views', 'shoestring'), namespace='cart')
    ),
    url(r'^accounts/',
        include(('shoestring.accounts.views', 'shoestring'), namespace='accounts')
    ),
    url(r'^products/',
        include(('shoestring.products.views', 'shoestring'), namespace='products')
    ),
    url(r'^order/',
        include(('shoestring.orders.views', 'shoestring'), namespace='orders')
    ),
]
