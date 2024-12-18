from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from config.settings import NUMBER_OF_PRODUCTS_DISPLAYED
from optics.models import Category, Product, Feedback, Service
from optics.src.utils import get_random_reviews, get_random_quote


def mainpage(request):

    category_list = Category.objects.filter(is_published=True)

    object_list = []
    for cat in category_list:
        product_set = Product.objects.filter(is_published=True, category=cat).order_by('?')
        product_list = product_set[:NUMBER_OF_PRODUCTS_DISPLAYED]
        obj = {'category': cat, 'product_list': product_list}
        object_list.append(obj)

    service_set = Service.objects.filter(is_published=True).order_by('?')
    service_list = service_set[:NUMBER_OF_PRODUCTS_DISPLAYED]

    context = {
        'object_list' : object_list,
        'category_list' : category_list,
        'service_list' : service_list,
        'testimonials' : get_random_reviews(),
        'quote' : get_random_quote()
    }

    return render(request, 'optics/index.html', context)


class FeedbackCreateView(CreateView):
    model = Feedback
    fields = ['name', 'phone', 'message']
    template_name = 'optics/contact.html'
    success_url = reverse_lazy('optics:thank-you')

def product_list_view(request):

    category_list = Category.objects.filter(is_published=True)

    object_list = []
    for cat in category_list:
        product_list = Product.objects.filter(is_published=True, category=cat).order_by('name')
        obj = {'category': cat, 'product_list': product_list}
        object_list.append(obj)

    context = {
        'object_list' : object_list,
        'category_list' : category_list,
        'testimonials' : get_random_reviews(),
        'quote' : get_random_quote()
    }

    return render(request, 'optics/shop_list.html', context)


class ServiceListView(ListView):
    model = Product
    template_name = 'optics/shop_list.html'
    # paginate_by = 3
    extra_context = {
    }
    ordering = ['name']

    def get_queryset(self):
        return Product.objects.filter(is_published=True)

def thank_you(request):
    context = {
    }

    return render(request, 'optics/thank-you.html', context=context)

def about(request):
    context = {
        'testimonials': get_random_reviews(),
    }
    return render(request, 'optics/about.html', context=context)