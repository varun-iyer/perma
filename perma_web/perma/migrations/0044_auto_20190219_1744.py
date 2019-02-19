# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-19 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perma', '0043_auto_20190123_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicallinkuser',
            name='cached_subscription_started',
            field=models.DateTimeField(blank=True, help_text="Used to help calculate how many links have been created against a paying customer's link limit.", null=True),
        ),
        migrations.AddField(
            model_name='historicalregistrar',
            name='cached_subscription_started',
            field=models.DateTimeField(blank=True, help_text="Used to help calculate how many links have been created against a paying customer's link limit.", null=True),
        ),
        migrations.AddField(
            model_name='linkuser',
            name='cached_subscription_started',
            field=models.DateTimeField(blank=True, help_text="Used to help calculate how many links have been created against a paying customer's link limit.", null=True),
        ),
        migrations.AddField(
            model_name='registrar',
            name='cached_subscription_started',
            field=models.DateTimeField(blank=True, help_text="Used to help calculate how many links have been created against a paying customer's link limit.", null=True),
        ),
    ]
