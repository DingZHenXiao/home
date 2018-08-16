# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-07-26 01:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_auto_20180725_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wife',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='index.Author')),
            ],
        ),
    ]
