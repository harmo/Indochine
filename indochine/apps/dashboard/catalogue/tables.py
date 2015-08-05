# -*- coding: utf-8 -*-
from django_tables2 import Column, TemplateColumn, A
from django.utils.translation import ugettext_lazy as _
from oscar.core.loading import get_class

DashboardTable = get_class('dashboard.tables', 'DashboardTable')


class ProductTable(DashboardTable):
    title = TemplateColumn(
        verbose_name=_('Title'),
        template_name='dashboard/catalogue/product_row_title.html',
        order_by='title', accessor=A('title'))
    image = TemplateColumn(
        verbose_name=_('Image'),
        template_name='dashboard/catalogue/product_row_image.html',
        orderable=False)
    product_class = Column(
        verbose_name=_('Product type'),
        accessor=A('product_class'),
        order_by='product_class__name')
    unity = Column(
        verbose_name='Unité de mesure',
        accessor=A('unity'))
    actions = TemplateColumn(
        verbose_name=_('Actions'),
        template_name='dashboard/catalogue/product_row_actions.html',
        orderable=False)

    icon = "sitemap"

    class Meta(DashboardTable.Meta):
        fields = ('date_updated', )
        sequence = ('title', 'image', 'product_class', 'unity', 'actions')
