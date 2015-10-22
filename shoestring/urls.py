from django.conf.urls import url, include


urlpatterns = [
    url(r'^cart/',
        include('shoestring.cart.urls', namespace='cart')),
    url(r'^accounts/',
        include('shoestring.accounts.urls', namespace='accounts')),
    url(r'^products/',
        include('shoestring.products.urls', namespace='products')),
]
