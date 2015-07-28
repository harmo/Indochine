# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0006_auto_20150728_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='suggest_on_home',
            field=models.BooleanField(default=False, verbose_name="Suggérer sur l'accueil"),
        ),
    ]
