# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0017_remove_product_tax'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_formula',
            field=models.BooleanField(default=False, verbose_name='Est uneformule ?'),
        ),
    ]
