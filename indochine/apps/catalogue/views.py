# -*- coding: utf-8 -*-
from django.db.models import Count
from oscar.apps.catalogue.views import (
    CatalogueView as CoreCatalogView,
    ProductDetailView as CoreProductDetailView)
from . import models


class CatalogueView(CoreCatalogView):
    template_name = 'card.html'

    def get_context_data(self, **kwargs):
        ctx = super(CatalogueView, self).get_context_data(**kwargs)
        ctx['products_by_category'] = self.get_products_by_category()
        return ctx

    def get_products_by_category(self):
        results = {}
        categories = models.Category\
            .get_tree()\
            .exclude(is_formula=True)\
            .annotate(nb_products=Count('product'))
        for inc, category in enumerate(categories):
            results[inc] = {
                'name': category.name,
                'image': category.image.url,
                'products': category.product_set.all(),
                'products_nb': category.nb_products}
        return results


class ProductDetailView(CoreProductDetailView):
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        ctx = super(ProductDetailView, self).get_context_data(**kwargs)
        ctx['suggests'] = models.Suggests.objects.all()
        ctx['recomanded_products'] = ctx['product'].recommended_products.all()
        return ctx


class FormulaView(CoreCatalogView):
    template_name = 'formulas.html'

    def get_context_data(self, **kwargs):
        ctx = super(FormulaView, self).get_context_data(**kwargs)
        ctx['products_by_formula'] = self.get_products_by_formula()
        return ctx

    def get_products_by_formula(self):
        results = {}
        categories = models.Category\
            .get_tree()\
            .exclude(is_formula=False)\
            .annotate(nb_products=Count('product'))
        for inc, category in enumerate(categories):
            results[inc] = {
                'name': category.name,
                'products': category.product_set.all(),
                'products_nb': category.nb_products}
        return results
