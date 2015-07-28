# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0008_remove_product_suggest_on_home'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='suggest_on_home',
            field=models.BooleanField(default=False),
        ),
    ]
