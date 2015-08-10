from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from oscar.app import application
from oscar.core.loading import get_class


catalogue_view = get_class('catalogue.views', 'CatalogueView')


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'la-carte/', include('indochine.apps.catalogue.urls', namespace='card')),
    url(r'', include(application.urls)),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
