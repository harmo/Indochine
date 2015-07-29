# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0009_product_suggest_on_home'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suggests',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='suggest_on_home',
        ),
        migrations.AddField(
            model_name='suggests',
            name='product',
            field=models.ForeignKey(to='catalogue.Product'),
        ),
    ]
