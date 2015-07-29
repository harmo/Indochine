# -*- coding: utf-8 -*-
from oscar.apps.dashboard.catalogue.forms import ProductForm as CoreProductForm


class ProductForm(CoreProductForm):

    class Meta(CoreProductForm.Meta):
        fields = [
            'title', 'description', 'suggest_on_home', 'is_discountable', 'structure']
