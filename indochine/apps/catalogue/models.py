from django.db import models
from oscar.apps.catalogue.abstract_models import *  # noqa


class Product(AbstractProduct):
    suggest_on_home = models.BooleanField(default=False, verbose_name='Suggérer sur la home ?')


from oscar.apps.catalogue.models import *
