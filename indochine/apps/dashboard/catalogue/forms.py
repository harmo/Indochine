# -*- coding: utf-8 -*-
from django import forms
from django.forms.models import inlineformset_factory
from oscar.apps.dashboard.catalogue.forms import (
    ProductForm as CoreProductForm,
    StockRecordForm as CoreStockRecordForm,
    StockRecordFormSet as CoreStockRecordFormSet)
from oscar.core.loading import get_model
from indochine.apps.partner.models import TAXES
from indochine.settings import OSCAR_DEFAULT_CURRENCY


Product = get_model('catalogue', 'Product')
StockRecord = get_model('partner', 'StockRecord')
Partner = get_model('partner', 'Partner')


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


class StockRecordForm(CoreStockRecordForm):
    fr_tax = forms.ChoiceField(
        choices=TAXES.CHOICES,
        required=False)

    ttc = forms.FloatField(
        required=False)

    partner_sku = forms.CharField(
        widget=forms.HiddenInput(),
        required=False)

    price_currency = forms.CharField(
        widget=forms.HiddenInput(),
        required=False)

    def __init__(self, product_class, user, *args, **kwargs):
        super(StockRecordForm, self).__init__(product_class, user, *args, **kwargs)
        self.fields['price_currency'].initial = OSCAR_DEFAULT_CURRENCY

    class Meta:
        model = StockRecord
        fields = [
            'num_in_stock', 'low_stock_threshold', 'partner',
            'price_excl_tax', 'fr_tax', 'cost_price', 'ttc'
        ]


BaseStockRecordFormSet = inlineformset_factory(
    Product, StockRecord, form=StockRecordForm, extra=1)


class StockRecordFormSet(BaseStockRecordFormSet, CoreStockRecordFormSet):
    def __init__(self, product_class, user, *args, **kwargs):
        super(StockRecordFormSet, self).__init__(product_class, user, *args, **kwargs)
