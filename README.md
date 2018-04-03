# shoestring
A very simple Single Page App eCommerce solution for Django

## Installation

Requires Python3 and Postgresql

### Frontend

Go into the frontend/ directory

Install required Node packages:

    $ npm install

Build the front end

    $ npm run build

This will put the new files in the static directory of the shoestring app.

### Backend

Install package and requirements:

    $ pipenv
    $ pip install shoestring/requirements.txt

Start a Django project:

    $ django-admin startproject shop
    $ cd shop

Add shoestring apps to INSTALLED_APPS

    $ vi shop/settings.py

    INSTALLED_APPS = [
      ...
      'shoestring',
      'shoestring.accounts',
      'shoestring.products',
      'shoestring.orders',
      'shoestring.payments',
      'easy_thumbnails',
    ]

Update the database settings:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'shoestring',
        }
    }

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

    path('shop/', include(('shoestring.urls', 'shoestring'), namespace='shoestring')),

Prime the database

    $ ./manage.py migrate
    ...
    $ ./manage.py runserver
