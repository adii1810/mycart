# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-04 07:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20200404_1227'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Orderupdate',
        ),
    ]