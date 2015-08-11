# -*- coding: utf-8 -*-
from oscar.apps.dashboard.catalogue.views import (
    ProductCreateUpdateView as CoreProductCreateUpdateView,
    CategoryCreateView as CoreCategoryCreateView,
    CategoryUpdateView as CoreCategoryUpdateView)
from oscar.core.loading import get_classes, get_model
from indochine.apps.partner.models import TAXES


(StockRecordFormSet, ) = get_classes('dashboard.catalogue.forms', (
    'StockRecordFormSet',))
Product = get_model('catalogue', 'Product')


class ProductCreateUpdateView(CoreProductCreateUpdateView):
    template_name = 'product_update.html'
    model = Product

    def get_context_data(self, **kwargs):
        ctx = super(ProductCreateUpdateView, self).get_context_data(**kwargs)
        ctx['TAXES'] = TAXES.CHOICES_DICT
        return ctx


class CategoryCreateView(CoreCategoryCreateView):
    template_name = 'category_form.html'


class CategoryUpdateView(CoreCategoryUpdateView):
    template_name = 'category_form.html'
