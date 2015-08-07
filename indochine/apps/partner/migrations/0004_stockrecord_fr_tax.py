# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0003_auto_20150604_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockrecord',
            name='fr_tax',
            field=models.IntegerField(verbose_name='Taxe', default=3, choices=[(1, 5.5), (2, 10), (3, 20)]),
        ),
    ]
