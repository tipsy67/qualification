from django.test import TestCase, Client
from django.urls import reverse

from optics.templatetags.optics_tags import add_media

from config.settings import NUMBER_OF_REVIEWS_DISPLAYED
from types import SimpleNamespace

from optics.models import Brand, Category, Product, Service
from optics.src.utils import get_random_reviews, get_random_quote
from tunes.models import Feedback, Quote


class OpticsAppTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.brand = Brand.objects.create(name='Brand for test')
        cls.category = Category.objects.create(name='Category for test')
        cls.product = Product.objects.create(name='Product for test', price=1.11, category=cls.category, brand=cls.brand)
        cls.service = Service.objects.create(name='Service for test', price=1.11)

    def test_brand_model(self):
        brand=Brand.objects.get(id=self.brand.pk)

        field_label = Brand._meta.get_field('name').verbose_name
        self.assertEqual(field_label,'Наименование')

        max_length = Brand._meta.get_field('name').max_length
        self.assertEqual(max_length,100)

        expected_object_name = '%s' % (brand.name)
        self.assertEqual(expected_object_name,str(brand))


    def test_category_model(self):
        category=Category.objects.get(id=self.category.pk)

        field_label = Category._meta.get_field('name').verbose_name
        self.assertEqual(field_label,'Наименование')
        field_label = Category._meta.get_field('description').verbose_name
        self.assertEqual(field_label,'Описание')
        field_label = Category._meta.get_field('is_published').verbose_name
        self.assertEqual(field_label,'Активно')
        field_label = Category._meta.get_field('active_on_main_page').verbose_name
        self.assertEqual(field_label,'Активно на гл.стр.')

        max_length = Category._meta.get_field('name').max_length
        self.assertEqual(max_length,100)

        expected_object_name = '%s' % (category.name)
        self.assertEqual(expected_object_name,str(category))

        self.assertEqual(category.is_published, False)
        self.assertEqual(category.active_on_main_page, False)



    def test_product_model(self):
        product=Product.objects.get(id=self.product.pk)

        field_label = Product._meta.get_field('name').verbose_name
        self.assertEqual(field_label,'Наименование')
        field_label = Product._meta.get_field('description').verbose_name
        self.assertEqual(field_label,'Описание')
        field_label = Product._meta.get_field('brand').verbose_name
        self.assertEqual(field_label,'Бренд')
        field_label = Product._meta.get_field('price').verbose_name
        self.assertEqual(field_label,'Цена')
        field_label = Product._meta.get_field('image').verbose_name
        self.assertEqual(field_label,'Изображение')
        field_label = Product._meta.get_field('created_at').verbose_name
        self.assertEqual(field_label,'Создан')
        field_label = Product._meta.get_field('update_at').verbose_name
        self.assertEqual(field_label,'Изменен')
        field_label = Product._meta.get_field('category').verbose_name
        self.assertEqual(field_label,'Категория')
        field_label = Product._meta.get_field('owner').verbose_name
        self.assertEqual(field_label,'Владелец')
        field_label = Product._meta.get_field('is_published').verbose_name
        self.assertEqual(field_label,'Активно')
        field_label = Product._meta.get_field('parameter').verbose_name
        self.assertEqual(field_label,'Параметр')

        max_length = Product._meta.get_field('name').max_length
        self.assertEqual(max_length,100)
        max_length = Product._meta.get_field('parameter').max_length
        self.assertEqual(max_length,30)

        max_digits = Product._meta.get_field('price').max_digits
        self.assertEqual(max_digits,15)
        decimal_places = Product._meta.get_field('price').decimal_places
        self.assertEqual(decimal_places,2)

        expected_object_name = '%s' % (product.name)
        self.assertEqual(expected_object_name,str(product))

        self.assertEqual(product.is_published, False)


    def test_service_model(self):
        service = Service.objects.get(id=self.service.pk)

        field_label = Service._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'Наименование')
        field_label = Service._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'Описание')
        field_label = Service._meta.get_field('duration').verbose_name
        self.assertEqual(field_label, 'Длительность')
        field_label = Service._meta.get_field('price').verbose_name
        self.assertEqual(field_label, 'Цена')
        field_label = Service._meta.get_field('image').verbose_name
        self.assertEqual(field_label, 'Изображение')
        field_label = Service._meta.get_field('medic').verbose_name
        self.assertEqual(field_label, 'medic')
        field_label = Service._meta.get_field('is_published').verbose_name
        self.assertEqual(field_label, 'Публиковать')

        max_length = Service._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

        max_digits = Service._meta.get_field('price').max_digits
        self.assertEqual(max_digits, 15)
        decimal_places = Service._meta.get_field('price').decimal_places
        self.assertEqual(decimal_places, 2)

        expected_object_name = '%s' % (service.name)
        self.assertEqual(expected_object_name, str(service))

        self.assertEqual(service.is_published, False)

    def test_views_main_page(self):
        url = reverse('optics:home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'optics/index.html')

    def test_views_FeedbackCreateView(self):
        url = reverse('optics:contact')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'optics/contact.html')

    def test_views_thank_you(self):
        url = reverse('optics:thank-you')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'optics/thank-you.html')

    def test_views_about(self):
        url = reverse('optics:about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'optics/about.html')

    def test_views_product_list_view(self):
        url = reverse('optics:shop-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'optics/shop_list.html')

    def test_views_service_list_view(self):
        url = reverse('optics:service-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'optics/service_list.html')

    def test_views_service_detail_view(self):
        url = reverse('optics:service-detail', args=[self.service.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'optics/service_detail.html')

    def test_optics_tags(self):
        self.assertEqual(add_media(None), "#")
        self.assertEqual(add_media("test.img"), "/media/test.img")

class OpticsUtilsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        count = 15
        for i in range(count+1):
            if i == count:
                Feedback.objects.create(name=f'Feedback for test {i}')
                Quote.objects.create(name='Quote for test {i}')
            else:
                Feedback.objects.create(name=f'Feedback for test {i}', is_published=True)
                Quote.objects.create(name='Quote for test {i}', is_published=True)

        # factory = RequestFactory()
        # cls.request = factory.get('optics:home')

        data_dict = {'session': {}}
        cls.request = SimpleNamespace(**data_dict)


    def test_get_random_reviews(self):
        test_set = get_random_reviews(self.request)

        self.assertEqual(len(test_set), NUMBER_OF_REVIEWS_DISPLAYED)

        for test_obj in test_set:
            self.assertEqual(test_obj.is_published, True)


    def test_get_random_quote(self):
        test_obj = get_random_quote(self.request)
        self.assertEqual(type(test_obj), Quote)
        self.assertEqual(test_obj.is_published, True)
