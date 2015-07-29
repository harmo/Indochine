# -*- coding: utf-8 -*-
from oscar.apps.promotions.views import HomeView as CoreHomeView
from indochine.apps.catalogue.models import Product


class HomeView(CoreHomeView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        ctx = super(HomeView, self).get_context_data(**kwargs)
        ctx['suggests'] = Product.objects.filter(suggest_on_home=True)
        return ctx
