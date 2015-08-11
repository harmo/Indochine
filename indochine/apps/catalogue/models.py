from django.db import models
from django.core.urlresolvers import reverse
from oscar.apps.catalogue.abstract_models import AbstractProduct, AbstractCategory


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
    add_desc = models.TextField(null=True, blank=True, verbose_name='Supplément de description')
    unity = models.CharField(max_length=50, null=True, blank=True, verbose_name='Unité de mesure')
    ingredients = models.TextField(null=True, blank=True, verbose_name='Ingrédients')

    def get_absolute_url(self):
        return reverse('card:detail',
                       kwargs={'product_slug': self.slug, 'pk': self.id})


class Category(AbstractCategory):
    is_formula = models.BooleanField(default=False, verbose_name='Est une formule ?')


from oscar.apps.catalogue.models import *  # noqa
