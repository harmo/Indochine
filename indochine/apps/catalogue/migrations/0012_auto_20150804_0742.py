# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def add_slider(apps, schema_editor):
    Slider = apps.get_model('catalogue', 'Slider')
    Slider.objects.create()


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0011_auto_20150804_0700'),
    ]

    operations = [
        migrations.RunPython(add_slider),
    ]
