from django.conf.urls import url
from .views import formula
from oscar.core.application import Application


class FormulaApplication(Application):
    name = None
    default_permissions = ['is_staff', ]

    def get_urls(self):
        urls = [
            url(r'^$', formula, name='formules'),
        ]
        return self.post_process_urls(urls)


application = FormulaApplication()
