from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from blog.models import Blog
from config.settings import MAIN_STREAMER_PATH, NUMBER_OF_PRODUCTS_DISPLAYED
from optics.models import Category, Product, Service
from tunes.models import Feedback
from optics.src.utils import get_random_quote, get_random_reviews


def main_page(request):

    category_list = Category.objects.filter(is_published=True)

    object_list = []
    for cat in category_list:
        product_set = Product.objects.filter(is_published=True, category=cat).order_by('?')
        product_list = product_set[:NUMBER_OF_PRODUCTS_DISPLAYED]
        obj = {'category': cat, 'product_list': product_list}
        object_list.append(obj)

    service_set = Service.objects.filter(is_published=True).order_by('?')
    service_list = service_set[:NUMBER_OF_PRODUCTS_DISPLAYED]

    blog_set = Blog.objects.filter(is_published=True).order_by('?')
    blog_list = blog_set[:3]

    context = {
        'object_list' : object_list,
        'category_list' : category_list,
        'service_list' : service_list,
        'blog_list' : blog_list,
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


def service_list_view(request):

    object_list = Service.objects.filter(is_published=True).order_by('name')

    streamer_content = {'title' : 'Наши услуги'}
    streamer_path = MAIN_STREAMER_PATH.copy()
    streamer_path.append({'name' : 'Услуги', 'url' : '#'})
    streamer_content['path'] = streamer_path

    context = {
        'object_list' : object_list,
        'testimonials' : get_random_reviews(),
        'quote' : get_random_quote(),
        'streamer_content' : streamer_content,
    }

    return render(request, 'optics/service_list.html', context)

def service_detail_view(request, pk):

    obj = Service.objects.filter(pk=pk).first()
    print (obj)

    streamer_content = {'title' : 'Наши услуги'}
    streamer_path = MAIN_STREAMER_PATH.copy()
    streamer_path.append({'name' : 'Услуги', 'url' : 'optics:service-list'})
    streamer_content['path'] = streamer_path
    streamer_path.append({'name' : 'Текущая', })
    streamer_content['path'] = streamer_path

    context = {
        'object' : obj,
        'testimonials' : get_random_reviews(),
        'quote' : get_random_quote(),
        'streamer_content' : streamer_content,
    }

    return render(request, 'optics/service_detail.html', context)

def thank_you(request):
    context = {
    }

    return render(request, 'optics/thank-you.html', context=context)

def about(request):
    streamer_content = {'title' : 'ОПТИКA СИТИ'}
    streamer_path = MAIN_STREAMER_PATH.copy()
    streamer_path.append({'name' : 'О нас', 'url' : '#'})
    streamer_content['path'] = streamer_path

    context = {
        'testimonials': get_random_reviews(),
        'streamer_content' : streamer_content
    }

    return render(request, 'optics/about.html', context=context)