# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-07 00:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='img_post'),
        ),
    ]
