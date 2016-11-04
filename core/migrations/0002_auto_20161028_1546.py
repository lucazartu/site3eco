# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 18:46
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('miniature_title', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=30)),
                ('miniature_image', models.ImageField(null=True, upload_to='portfolio/miniatures/%Y/%m/%d')),
                ('project_name', models.CharField(max_length=30)),
                ('intro', models.CharField(max_length=30)),
                ('image', models.ImageField(null=True, upload_to='portfolio/images/%Y/%m/%d')),
                ('description', ckeditor.fields.RichTextField()),
                ('date', models.DateField()),
                ('client', models.CharField(max_length=20)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='thumb',
            field=models.ImageField(null=True, upload_to='thumbs/%Y/%m/%d/'),
        ),
    ]