from django.db import models
from oscar.apps.catalogue.abstract_models import *  # noqa


class Product(AbstractProduct):
    suggest_on_home = models.BooleanField(default=False)


from oscar.apps.catalogue.models import *
