from django.conf.urls import include, url

urlpatterns = [
    url(r'^cart/',
        include('shoestring.cart.urls', namespace='cart')),
    url(r'^accounts/',
        include('shoestring.accounts.urls', namespace='accounts')),
    url(r'^products/',
        include('shoestring.products.urls', namespace='products')),
]
