# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0012_auto_20150804_0742'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='subtitle',
            field=models.CharField(verbose_name='Sous-titre', blank=True, null=True, max_length=150),
        ),
        migrations.AddField(
            model_name='product',
            name='unity',
            field=models.CharField(verbose_name='Unité de mesure', blank=True, null=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='sliderimages',
            name='image',
            field=models.ImageField(upload_to='homepage_slider'),
        ),
    ]
