# -*- coding: utf-8 -*-
from oscar.apps.dashboard.catalogue.views import ProductCreateUpdateView as CoreProductCreateUpdateView


class ProductCreateUpdateView(CoreProductCreateUpdateView):
    template_name = 'product_update.html'
