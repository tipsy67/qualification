from django.shortcuts import render

from optics.models import Category, Product


def mainpage(request):

    category_list = Category.objects.filter(is_published=True)

    product_set = Product.objects.filter(is_published=True).order_by('?')
    product_list = product_set[:4]

    context = {
        'product_list' : product_list,
        'category_list' : category_list
    }

    return render(request, 'optics/index.html', context)
