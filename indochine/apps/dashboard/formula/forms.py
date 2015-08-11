from django import forms
from oscar.core.loading import get_model

# Suggests = get_model('catalogue', 'Suggests')
Product = get_model('catalogue', 'Product')


class FormulaLeftForm(forms.Form):
    title = forms.CharField(
        label='Titre')

    subtitle = forms.CharField(
        label='Sous-titre')

    description = forms.CharField(
        label='Description',
        widget=forms.widgets.Textarea())


class FormulaRightForm(forms.Form):
    product = forms.ModelChoiceField(
        label="Choisir un produit",
        empty_label="-- Choisir --",
        queryset=Product.objects.all())

    ttc = forms.FloatField(
        label='TTC modifié',
        required=False)
