# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-01 18:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20161019_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
