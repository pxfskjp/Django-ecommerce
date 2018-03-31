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
        include(('shoestring.cart.urls', 'shoestring'), namespace='cart')
    ),
    url(r'^accounts/',
        include(('shoestring.accounts.urls', 'shoestring'), namespace='accounts')
    ),
    url(r'^products/',
        include(('shoestring.products.urls', 'shoestring'), namespace='products')
    ),
    url(r'^order/',
        include(('shoestring.orders.urls', 'shoestring'), namespace='orders')
    ),
]
