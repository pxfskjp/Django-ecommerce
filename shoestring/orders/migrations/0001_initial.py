# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('shipping_address', models.TextField(blank=True)),
                ('shipping_suburb', models.CharField(max_length=100, blank=True)),
                ('shipping_postcode', models.CharField(max_length=6, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('sku', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(max_digits=8, decimal_places=2)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('status', models.IntegerField(default=0, choices=[(-1, 'CANCELLED'), (0, 'PENDING'), (1, 'SHIPPED')])),
                ('brand', models.ForeignKey(to='products.Brand')),
                ('order', models.ForeignKey(related_name='items', to='orders.Order')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
