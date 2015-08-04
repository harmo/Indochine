from django.conf.urls import url
from indochine.apps.dashboard.homepage.views import homepage_suggestions, homepage_slider
from oscar.core.application import Application


class HomepageApplication(Application):
    name = None
    default_permissions = ['is_staff', ]

    def get_urls(self):
        urls = [
            url(r'^suggestions$', homepage_suggestions, name='homepage_suggestions'),
            url(r'^slider$', homepage_slider, name='homepage_slider'),
        ]
        return self.post_process_urls(urls)


application = HomepageApplication()
