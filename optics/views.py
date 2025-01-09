from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.decorators.cache import cache_page
from django.views.generic import CreateView, ListView
from django.core.paginator import Paginator

from blog.models import Blog
from config.settings import MAIN_STREAMER_PATH, NUMBER_OF_PRODUCTS_DISPLAYED, SERVICE_PER_PAGE, PRODUCT_PER_PAGE
from optics.models import Category, Product, Service
from optics.src.utils import get_random_quote, get_random_reviews
from tunes.models import Feedback, TunesDict, Banner


@cache_page(600)
def main_page(request):

    banner_list = Banner.objects.filter(is_published=True)

    category_list = Category.objects.filter(is_published=True)

    object_list = []
    for cat in category_list:
        product_set = Product.objects.filter(is_published=True, category=cat).order_by(
            '?'
        )
        product_list = product_set[:NUMBER_OF_PRODUCTS_DISPLAYED]
        obj = {'category': cat, 'product_list': product_list}
        object_list.append(obj)

    service_set = Service.objects.filter(is_published=True).order_by('?')
    service_list = service_set[:NUMBER_OF_PRODUCTS_DISPLAYED]

    blog_set = Blog.objects.filter(is_published=True).order_by('?')
    blog_list = blog_set[:3]

    context = {
        'object_list': object_list,
        'category_list': category_list,
        'service_list': service_list,
        'blog_list': blog_list,
        'testimonials': get_random_reviews(request),
        'quote': get_random_quote(request),
        'banner_list': banner_list,
    }

    return render(request, 'optics/index.html', context)


class FeedbackCreateView(CreateView):
    model = Feedback
    fields = ['name', 'phone', 'message']
    template_name = 'optics/contact.html'
    success_url = reverse_lazy('optics:thank-you')

    streamer_content = {'title': "Контакты"}
    streamer_path = MAIN_STREAMER_PATH.copy()
    streamer_path.append({'name': "Контакты", 'url': "#"})
    streamer_content['path'] = streamer_path
    extra_context = {
        'streamer_content': streamer_content,
    }


@cache_page(600)
def product_list_view(request):

    category_list = Category.objects.filter(is_published=True)

    object_list = []
    for cat in category_list:
        product_list = Product.objects.filter(is_published=True, category=cat).order_by(
            'name'
        )
        paginator = Paginator(product_list, PRODUCT_PER_PAGE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # obj = {'category': cat, 'product_list': product_list}
        obj = {'category': cat, 'page_obj': page_obj}
        object_list.append(obj)

    streamer_content = {'title': "Наши товары"}
    streamer_path = MAIN_STREAMER_PATH.copy()
    streamer_path.append({'name': "Магазин", 'url': "#"})
    streamer_content['path'] = streamer_path

    context = {
        'object_list': object_list,
        'category_list': category_list,
        'testimonials': get_random_reviews(request),
        'quote': get_random_quote(request),
        'streamer_content': streamer_content,
    }

    return render(request, 'optics/shop_list.html', context)


@cache_page(600)
def service_list_view(request):

    object_list = Service.objects.filter(is_published=True).order_by('name')

    paginator = Paginator(object_list, SERVICE_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    streamer_content = {'title': "Наши услуги"}
    streamer_path = MAIN_STREAMER_PATH.copy()
    streamer_path.append({'name': "Услуги", 'url': "#"})
    streamer_content['path'] = streamer_path

    context = {
        'testimonials': get_random_reviews(request),
        'quote': get_random_quote(request),
        'streamer_content': streamer_content,
        'page_obj': page_obj,
    }

    return render(request, 'optics/service_list.html', context)


@cache_page(600)
def service_detail_view(request, pk):

    obj = Service.objects.filter(pk=pk).first()

    streamer_content = {'title': "Наши услуги"}
    streamer_path = MAIN_STREAMER_PATH.copy()
    streamer_path.append({'name': "Услуги", 'url': "optics:service-list"})
    streamer_path.append(
        {
            'name': 'Текущая',
        }
    )
    streamer_content['path'] = streamer_path

    context = {
        'object': obj,
        'testimonials': get_random_reviews(request),
        'quote': get_random_quote(request),
        'streamer_content': streamer_content,
    }

    return render(request, 'optics/service_detail.html', context)


@cache_page(600)
def thank_you(request):
    context = {}

    return render(request, 'optics/thank-you.html', context=context)


@cache_page(600)
def about(request):
    streamer_content = {'title': "ОПТИКA СИТИ"}
    streamer_path = MAIN_STREAMER_PATH.copy()
    streamer_path.append({'name': "О нас", 'url': "#"})
    streamer_content['path'] = streamer_path

    context = {
        'testimonials': get_random_reviews(request),
        'streamer_content': streamer_content,
    }

    return render(request, 'optics/about.html', context=context)
