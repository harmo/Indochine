# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0004_stockrecord_fr_tax'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockrecord',
            name='fr_tax',
            field=models.IntegerField(default=3, verbose_name='Taxe', choices=[(0, ''), (1, 5.5), (2, 10), (3, 20)]),
        ),
    ]
