from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',
        views.ProductListView.as_view(),
        name='product-list'),
    url(r'^(?P<alias>[\w-]+)/(?P<path>.*)$',
        views.thumbnail,
        name='thumbnail'),
]
