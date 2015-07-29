from oscar.apps.dashboard.catalogue.tables import ProductTable as CoreProductTable

from django_tables2 import TemplateColumn

from oscar.core.loading import get_class

DashboardTable = get_class('dashboard.tables', 'DashboardTable')


class ProductTable(CoreProductTable):
    suggest_on_home = TemplateColumn(
        template_name='dashboard/suggest_on_home.html',)

    class Meta(DashboardTable.Meta):
        sequence = ('title', 'image', 'product_class', 'suggest_on_home', 'upc', 'variants',
                    'stock_records', 'date_updated', 'actions')
