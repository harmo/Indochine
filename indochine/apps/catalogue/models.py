from django.db import models
# from oscar.apps.catalogue.models import Product as CoreProduct
from oscar.apps.catalogue.abstract_models import AbstractProduct


class Suggests(models.Model):
    product = models.ForeignKey('Product')

    class Meta:
        verbose_name = 'Suggestion'


class Slider(models.Model):
    pass


class SliderImages(models.Model):
    slider = models.ForeignKey(Slider)
    image = models.ImageField(upload_to='homepage_slider')


class Product(AbstractProduct):
    subtitle = models.CharField(max_length=150, null=True, blank=True, verbose_name='Sous-titre')
    unity = models.CharField(max_length=50, null=True, blank=True, verbose_name='Unité de mesure')


from oscar.apps.catalogue.models import *  # noqa
