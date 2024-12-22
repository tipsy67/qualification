from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from config.settings import MAIN_STREAMER_PATH, NUMBER_OF_PRODUCTS_DISPLAYED
from optics.models import Category, Feedback, Product, Service
from optics.src.utils import get_random_quote, get_random_reviews


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

    streamer_content = {'title' : 'Контакты'}
    streamer_path = MAIN_STREAMER_PATH.copy()
    streamer_path.append({'name' : 'Контакты', 'url' : '#'})
    streamer_content['path'] = streamer_path
    extra_context = {
        'streamer_content' : streamer_content,
    }

def product_list_view(request):

    category_list = Category.objects.filter(is_published=True)

    object_list = []
    for cat in category_list:
        product_list = Product.objects.filter(is_published=True, category=cat).order_by('name')
        obj = {'category': cat, 'product_list': product_list}
        object_list.append(obj)

    streamer_content = {'title' : 'Наши товары'}
    streamer_path = MAIN_STREAMER_PATH.copy()
    streamer_path.append({'name' : 'Магазин', 'url' : '#'})
    streamer_content['path'] = streamer_path

    context = {
        'object_list' : object_list,
        'category_list' : category_list,
        'testimonials' : get_random_reviews(),
        'quote' : get_random_quote(),
        'streamer_content' : streamer_content,
    }

    return render(request, 'optics/shop_list.html', context)


class ServiceListView(ListView):
    model = Product
    template_name = 'optics/shop_list.html'
    # paginate_by = 3

    streamer_content = {'title' : 'Контакты'}
    streamer_path = MAIN_STREAMER_PATH.copy()
    streamer_path.append({'name' : 'Контакты', 'url' : '#'})
    streamer_content['path'] = streamer_path

    extra_context = {
        'streamer_content' : streamer_content,
    }
    ordering = ['name']

    def get_queryset(self):
        return Product.objects.filter(is_published=True)

def thank_you(request):
    context = {
    }

    return render(request, 'optics/thank-you.html', context=context)

def about(request):
    streamer_content = {'title' : 'ОПТИК СИТИ'}
    streamer_path = MAIN_STREAMER_PATH.copy()
    streamer_path.append({'name' : 'о нас', 'url' : '#'})
    streamer_content['path'] = streamer_path

    context = {
        'testimonials': get_random_reviews(),
        'streamer_content' : streamer_content
    }

    return render(request, 'optics/about.html', context=context)