# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-02 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20190702_1645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posttype',
            name='ad',
        ),
        migrations.AddField(
            model_name='posttype',
            name='seri',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
