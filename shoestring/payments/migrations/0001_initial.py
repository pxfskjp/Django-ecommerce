# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(editable=False, default=django.utils.timezone.now)),
                ('state', models.IntegerField(default=0, choices=[(-1, 'Cancelled'), (0, 'Pending'), (1, 'Declined'), (2, 'Approved')])),
                ('amount', models.DecimalField(max_digits=8, decimal_places=2)),
                ('reason', models.CharField(max_length=200, blank=True)),
                ('order', models.ForeignKey(to='orders.Order')),
            ],
        ),
    ]
