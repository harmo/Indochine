from django.utils.translation import ungettext_lazy
from django_tables2 import LinkColumn, TemplateColumn, A
from oscar.core.loading import get_class, get_model


DashboardTable = get_class('dashboard.tables', 'DashboardTable')
Suggests = get_model('catalogue', 'Suggests')
SliderImages = get_model('catalogue', 'SliderImages')


class SuggestsTable(DashboardTable):
    product = LinkColumn(
        'dashboard:catalogue-product',
        args=[A('product.pk')],
        verbose_name='Produit')

    delete = TemplateColumn(
        template_name='suggest-delete.html',
        verbose_name=' ',
        orderable=False)

    icon = 'sitemap'
    caption = ungettext_lazy("%s suggestion", "%s suggestions")

    class Meta(DashboardTable.Meta):
        model = Suggests
        fields = ('product', )


class SliderTable(DashboardTable):
    image = TemplateColumn(
        template_name='slider-image.html',
        orderable=False)

    delete = TemplateColumn(
        template_name='slider-image-delete.html',
        verbose_name=' ',
        orderable=False)

    icon = 'picture'
    caption = ungettext_lazy("%s image", "%s images")

    class Meta(DashboardTable.Meta):
        model = SliderImages
        fields = ('image',)
