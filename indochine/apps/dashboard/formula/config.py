from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class FormulaDashboardConfig(AppConfig):
    label = 'formula_dashboard'
    name = 'indochine.apps.dashboard.formula'
    verbose_name = _('Formula dashboard')
