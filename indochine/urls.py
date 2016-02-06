from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from oscar.app import application
from oscar.core.loading import get_class


catalogue_view = get_class('catalogue.views', 'CatalogueView')


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'la-carte/', include('indochine.apps.catalogue.urls', namespace='card')),
    url(r'mon-compte/', TemplateView.as_view(template_name='static-pages/account.html'), name='account'),
    url(r'qui-sommes-nous/', TemplateView.as_view(template_name='static-pages/us.html'), name='us'),
    url(r'groupes-et-pros/', TemplateView.as_view(template_name='static-pages/groups-and-pros.html'), name='pros'),
    url(r'contact/', TemplateView.as_view(template_name='static-pages/contact.html'), name='contact'),
    url(r'', include(application.urls)),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
