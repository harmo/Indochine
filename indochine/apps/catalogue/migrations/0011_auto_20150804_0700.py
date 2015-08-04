# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0010_auto_20150729_1209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='SliderImages',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to='')),
                ('slider', models.ForeignKey(to='catalogue.Slider')),
            ],
        ),
        migrations.AlterModelOptions(
            name='suggests',
            options={'verbose_name': 'Suggestion'},
        ),
    ]
