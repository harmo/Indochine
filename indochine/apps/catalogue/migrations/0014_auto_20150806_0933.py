# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0013_auto_20150804_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='add_desc',
            field=models.TextField(blank=True, max_length=255, verbose_name='Supplément de description', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='ingredients',
            field=models.TextField(blank=True, max_length=255, verbose_name='Ingrédients', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='short_desc',
            field=models.TextField(blank=True, max_length=255, verbose_name='Description courte', null=True),
        ),
    ]
