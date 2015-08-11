# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0018_category_is_formula'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='is_formula',
        ),
        migrations.AddField(
            model_name='productcategory',
            name='is_formula',
            field=models.BooleanField(verbose_name='Est une formule ?', default=False),
        ),
    ]
