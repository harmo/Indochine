from django import forms
from django.utils.translation import ugettext_lazy as _
from oscar.core.loading import get_model

Suggests = get_model('catalogue', 'Suggests')
Product = get_model('catalogue', 'Product')


class ProductSelectForm(forms.Form):
    product = forms.ModelChoiceField(
        label=_("Choisir un produit"),
        empty_label=_("-- Choisir --"),
        queryset=Product.objects.all().exclude(pk__in=Suggests.objects.all().values('product__pk')))


class SliderForm(forms.Form):
    image = forms.ImageField()
