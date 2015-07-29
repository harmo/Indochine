from django.conf.urls import url
from indochine.apps.dashboard.homepage.views import homepage
from oscar.core.application import Application


class HomepageApplication(Application):
    name = None
    default_permissions = ['is_staff', ]

    def get_urls(self):
        urls = [
            url(r'^$', homepage, name='homepage'),
        ]
        return self.post_process_urls(urls)


application = HomepageApplication()
