from django.shortcuts import render
from django_tables2 import RequestConfig
from indochine.apps.dashboard.homepage.tables import SuggestsTable
from indochine.apps.dashboard.homepage.forms import ProductSelectForm
from oscar.core.loading import get_model

Suggests = get_model('catalogue', 'Suggests')
Product = get_model('catalogue', 'Product')


def homepage(request):
    if request.POST and request.POST.get('product') != '':
        product = Product.objects.get(pk=int(request.POST.get('product')))
        Suggests.objects.create(product=product)

    elif request.GET:
        if 'delete-suggest' in request.GET and request.GET.get('delete-suggest') != '':
            Suggests.objects.get(pk=int(request.GET.get('delete-suggest'))).delete()

    table = SuggestsTable(Suggests.objects.all())
    RequestConfig(request).configure(table)

    return render(request, 'dashboard/suggests.html', {
        'suggests': table,
        'suggest_form': ProductSelectForm})
