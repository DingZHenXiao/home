# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-08-03 03:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('spec', models.CharField(max_length=20)),
                ('picture', models.ImageField(upload_to='static/upload/goods')),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('picture', models.ImageField(upload_to='static/upload/goodstype')),
                ('desc', models.TextField()),
            ],
        ),
    ]
