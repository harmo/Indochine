# -*- coding: utf-8 -*-
from oscar.apps.dashboard.catalogue.views import ProductCreateUpdateView as CoreProductCreateUpdateView
from oscar.core.loading import get_classes
from oscar.core.utils import slugify
from indochine.apps.partner.models import TAXES


(StockRecordFormSet, ) = get_classes('dashboard.catalogue.forms', (
    'StockRecordFormSet',))


class ProductCreateUpdateView(CoreProductCreateUpdateView):
    template_name = 'product_update.html'

    def get_context_data(self, **kwargs):
        ctx = super(ProductCreateUpdateView, self).get_context_data(**kwargs)
        ctx['TAXES'] = TAXES.CHOICES_DICT
        return ctx

    def process_all_forms(self, form):
        formsets = {}
        for ctx_name, formset_class in self.formsets.items():
            formsets[ctx_name] = formset_class(self.product_class,
                                               self.request.user,
                                               self.request.POST,
                                               self.request.FILES,
                                               instance=self.object)

        stockrecord_formset = formsets.get('stockrecord_formset')
        # if stockrecord_formset.data['stockrecords-0-partner'] is not None:
        stockrecord_formset.data['stockrecords-0-partner_sku'] = '{partner}{label}'.format(
            partner=slugify(stockrecord_formset.data.get('stockrecords-0-partner')),
            label=slugify(stockrecord_formset.data.get('title')))

        if self.creating and form.is_valid():
            self.object = form.save()

        formsets = {}
        for ctx_name, formset_class in self.formsets.items():
            formsets[ctx_name] = formset_class(self.product_class,
                                               self.request.user,
                                               self.request.POST,
                                               self.request.FILES,
                                               instance=self.object)

        is_valid = form.is_valid() and all([formset.is_valid()
                                            for formset in formsets.values()])

        cross_form_validation_result = self.clean(form, formsets)
        if is_valid and cross_form_validation_result:
            return self.forms_valid(form, formsets)
        else:
            return self.forms_invalid(form, formsets)

    form_valid = process_all_forms
