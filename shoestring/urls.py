from django.conf.urls import include, url
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie


urlpatterns = [
    url(r'^$',
        ensure_csrf_cookie(render),
        {'template_name': 'shoestring/index.html'},
        name='index'),
    url(r'^cart/', render, 
        include('shoestring.cart.urls', namespace='cart')),
    url(r'^accounts/',
        include('shoestring.accounts.urls', namespace='accounts')),
    url(r'^products/',
        include('shoestring.products.urls', namespace='products')),
]
