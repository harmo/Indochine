# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0015_remove_product_short_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tax',
            field=models.BooleanField(choices=[(1, 0.055), (2, 0.1), (3, 0.2)], default=3),
        ),
        migrations.AlterField(
            model_name='product',
            name='add_desc',
            field=models.TextField(verbose_name='Supplément de description', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='ingredients',
            field=models.TextField(verbose_name='Ingrédients', null=True, blank=True),
        ),
    ]
