# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import oscar.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0005_auto_20150604_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productattribute',
            name='code',
            field=models.SlugField(max_length=128, validators=[django.core.validators.RegexValidator(message="Code can only contain the letters a-z, A-Z, digits, and underscores, and can't start with a digit", regex='^[a-zA-Z_][0-9a-zA-Z_]*$'), oscar.core.validators.non_python_keyword], verbose_name='Code'),
        ),
    ]
