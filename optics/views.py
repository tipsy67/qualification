from django.shortcuts import render

from optics.models import Category, Product
from optics.src.utils import get_random_reviews, get_random_quote


def mainpage(request):

    category_list = Category.objects.filter(is_published=True)

    object_list = []
    for cat in category_list:
        product_set = Product.objects.filter(is_published=True, category=cat).order_by('?')
        product_list = product_set[:4]
        obj = {'category': cat, 'product_list': product_list}
        object_list.append(obj)

    context = {
        'object_list' : object_list,
        'category_list' : category_list,
        'testimonials' : get_random_reviews(),
        'quote' : get_random_quote()
    }

    return render(request, 'optics/index.html', context)
