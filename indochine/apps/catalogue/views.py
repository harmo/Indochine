# -*- coding: utf-8 -*-
from oscar.apps.catalogue.views import CatalogueView as CoreCatalogView
from . import models


class CatalogueView(CoreCatalogView):
    template_name = 'browse.html'

    def get_context_data(self, **kwargs):
        ctx = super(CatalogueView, self).get_context_data(**kwargs)
        ctx['products_by_category'] = self.get_products_by_category()
        return ctx

    def get_products_by_category(self):
        results = {}
        for category in models.Category.objects.all():
            results[category.name] = {
                'image': category.image.url,
                'products': category.product_set.all()}
        return results
