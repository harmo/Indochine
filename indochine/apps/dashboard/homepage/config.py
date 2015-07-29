from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class HomepageDashboardConfig(AppConfig):
    label = 'homepage_dashboard'
    name = 'indochine.apps.dashboard.homepage'
    verbose_name = _('Homepage dashboard')
