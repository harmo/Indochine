# -*- coding: utf-8 -*-
from django.db.models import Count
from oscar.apps.catalogue.views import (
    CatalogueView as CoreCatalogView,
    ProductDetailView as CoreProductDetailView)
from . import models


class CatalogueView(CoreCatalogView):
    template_name = 'browse.html'

    def get_context_data(self, **kwargs):
        ctx = super(CatalogueView, self).get_context_data(**kwargs)
        ctx['products_by_category'] = self.get_products_by_category()
        return ctx

    def get_products_by_category(self):
        results = {}
        inc = 0
        for category in models.Category.get_tree().annotate(nb_products=Count('product')):
            results[inc] = {
                'name': category.name,
                'image': category.image.url,
                'products': category.product_set.all(),
                'products_nb': category.nb_products}
            inc += 1
        return results


class ProductDetailView(CoreProductDetailView):
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        ctx = super(ProductDetailView, self).get_context_data(**kwargs)
        ctx['suggests'] = models.Suggests.objects.all()
        ctx['recomanded_products'] = ctx['product'].recommended_products.all()
        return ctx
