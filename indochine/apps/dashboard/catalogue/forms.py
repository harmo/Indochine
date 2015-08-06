# -*- coding: utf-8 -*-
from django import forms
from oscar.apps.dashboard.catalogue.forms import ProductForm as CoreProductForm
from oscar.core.loading import get_model


Product = get_model('catalogue', 'Product')


class ProductSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255, required=False, label='Nom du produit')

    def clean(self):
        cleaned_data = super(ProductSearchForm, self).clean()
        cleaned_data['title'] = cleaned_data['title'].strip()
        return cleaned_data


class ProductForm(CoreProductForm):
    class Meta:
        model = Product
        fields = [
            'title', 'subtitle', 'unity', 'description', 'add_desc', 'ingredients']
