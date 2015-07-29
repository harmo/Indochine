from django.db import models
from oscar.apps.catalogue.models import Product


class Suggests(models.Model):
    product = models.ForeignKey(Product)

    class Meta:
        verbose_name = 'Suggestion'


from oscar.apps.catalogue.models import * # noqa
