# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import array_tags.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/')),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(max_digits=8, decimal_places=2)),
                ('enabled', models.BooleanField(default=False, db_index=True)),
                ('tags', array_tags.fields.TagField(size=None, base_field=models.CharField(max_length=50), blank=True)),
                ('brand', models.ForeignKey(to='products.Brand')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='image',
            name='product',
            field=models.ForeignKey(related_name='images', to='products.Product'),
        ),
    ]
