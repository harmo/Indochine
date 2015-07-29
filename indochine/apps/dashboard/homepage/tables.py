from django.utils.translation import ungettext_lazy
from django_tables2 import LinkColumn, TemplateColumn, A
from oscar.core.loading import get_class, get_model


DashboardTable = get_class('dashboard.tables', 'DashboardTable')
Suggests = get_model('catalogue', 'Suggests')


class SuggestsTable(DashboardTable):
    product = LinkColumn(
        'dashboard:catalogue-product',
        args=[A('product.pk')],
        verbose_name='Produit')

    delete = TemplateColumn(
        template_name='dashboard/suggest-delete.html',
        verbose_name=' ',
        orderable=False)

    icon = 'sitemap'
    caption = ungettext_lazy("%s Suggestion", "%s Suggestions")

    class Meta(DashboardTable.Meta):
        model = Suggests
        fields = ('product', )
