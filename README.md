# shoestring
A very simple ecommerce solution for Django

## Installation

Requires Python3 and Postgresql

Install package and requirements:

  $ pip install shoestring
  $ pip install shoestring/requirements.txt

Start a Django project:

  $ django-admin startproject shop
  $ cd shop

Add shoestring apps to INSTALLED_APPS

  $ vi shop/settings.py
  
    'shoestring',
    'shoestring.accounts',
    'shoestring.products',
    'shoestring.orders',
    'shoestring.payments',

    'easy_thumbnails',

Use our User model:

    AUTH_USER_MODEL = 'accounts.User'

Add default easy-thumbnails settings:

    THUMBNAIL_ALIASES = {
        '': {
            'product-list': {
                'size': (90, 120),
                'upscale': True,
                'crop': 'auto'
            },
        },
    }

Hook in the urls:

  $ vi shop/urls.py

    url(r'^api/', include('shoestring.urls', namespace='shoestring')),

Prime the database

  $ ./manage.py syncdb
  ...
  $ ./manage.py runserver
