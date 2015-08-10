from django.conf.urls import url, include
from oscar.core.loading import get_class

from oscar.apps.dashboard.app import DashboardApplication as CoreDashboardApplication


class DashboardApplication(CoreDashboardApplication):
    homepage_app = get_class('dashboard.homepage.app', 'application')
    formula_app = get_class('dashboard.formula.app', 'application')

    def get_urls(self):
        urls = CoreDashboardApplication.get_urls(self) + [
            url(r'^homepage/', include(self.homepage_app.urls)),
            url(r'^formula/', include(self.formula_app.urls))
        ]
        return self.post_process_urls(urls)


application = DashboardApplication()
