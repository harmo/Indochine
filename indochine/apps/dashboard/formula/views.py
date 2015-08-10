from django.shortcuts import render
from django_tables2 import RequestConfig
from indochine.apps.dashboard.homepage.tables import SuggestsTable, SliderTable
from indochine.apps.dashboard.homepage.forms import ProductSelectForm, SliderForm
from oscar.core.loading import get_model

# Suggests = get_model('catalogue', 'Suggests')
# Product = get_model('catalogue', 'Product')
# Slider = get_model('catalogue', 'Slider')
# SliderImages = get_model('catalogue', 'SliderImages')


def formula(request):
    return render(request, 'formula.html', {
        'products_form': ProductSelectForm})


# def homepage_suggestions(request):
#     if request.POST and request.POST.get('product') != '':
#         product = Product.objects.get(pk=int(request.POST.get('product')))
#         Suggests.objects.create(product=product)

#     elif request.GET:
#         if 'delete-suggest' in request.GET and request.GET.get('delete-suggest') != '':
#             Suggests.objects.get(pk=int(request.GET.get('delete-suggest'))).delete()

#     table = SuggestsTable(Suggests.objects.all())
#     RequestConfig(request).configure(table)

#     return render(request, 'suggests.html', {
#         'suggests': table,
#         'suggest_form': ProductSelectForm})


# def homepage_slider(request):
#     if request.FILES and request.FILES.get('image') != '':
#         slider = Slider.objects.get(pk=1)
#         slider_image = SliderImages(
#             slider=slider,
#             image=request.FILES.get('image')
#         )
#         slider_image.save()

#     elif request.GET:
#         if 'delete-image' in request.GET and request.GET.get('delete-image') != '':
#             SliderImages.objects.get(pk=int(request.GET.get('delete-image'))).delete()

#     table = SliderTable(SliderImages.objects.all())
#     RequestConfig(request).configure(table)

#     return render(request, 'slider.html', {
#         'slider': table,
#         'slider_form': SliderForm})
