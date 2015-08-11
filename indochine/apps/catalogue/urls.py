from django.conf.urls import url
from oscar.core.loading import get_class


catalogue_view = get_class('catalogue.views', 'CatalogueView')
formula_view = get_class('catalogue.views', 'FormulaView')
detail_view = get_class('catalogue.views', 'ProductDetailView')


urlpatterns = [
    url(r'^$', catalogue_view.as_view(), name='list'),
    url(r'^nos-formules/$', formula_view.as_view(), name='formula'),
    url(r'^(?P<product_slug>[\w-]*)_(?P<pk>\d+)/$', detail_view.as_view(), name='detail'),
]
