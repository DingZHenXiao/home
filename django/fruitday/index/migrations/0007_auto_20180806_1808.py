# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-08-06 10:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_carinto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carinto',
            old_name='goods',
            new_name='good',
        ),
    ]
