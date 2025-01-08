from django.test import TestCase

from blog.models import Blog


class OpticsAppTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Blog.objects.create(title='Blog for test')

    def test_blog_model(self):
        blog=Blog.objects.get(id=1)

        field_label = Blog._meta.get_field('title').verbose_name
        self.assertEqual(field_label,'Заголовок')
        field_label = Blog._meta.get_field('slug').verbose_name
        self.assertEqual(field_label,'Slug')
        field_label = Blog._meta.get_field('image').verbose_name
        self.assertEqual(field_label,'Изображение')
        field_label = Blog._meta.get_field('created_at').verbose_name
        self.assertEqual(field_label,'Создан')
        field_label = Blog._meta.get_field('update_at').verbose_name
        self.assertEqual(field_label,'Изменен')
        field_label = Blog._meta.get_field('is_published').verbose_name
        self.assertEqual(field_label,'Признак публикации')
        field_label = Blog._meta.get_field('views_counter').verbose_name
        self.assertEqual(field_label,'Количество просмотров')
        field_label = Blog._meta.get_field('content').verbose_name
        self.assertEqual(field_label,'Содержимое')
        field_label = Blog._meta.get_field('owner').verbose_name
        self.assertEqual(field_label,'Владелец')

        max_length = Blog._meta.get_field('title').max_length
        self.assertEqual(max_length,100)
        max_length = Blog._meta.get_field('slug').max_length
        self.assertEqual(max_length,100)

        expected_object_name = '%s' % (blog.title)
        self.assertEqual(expected_object_name,str(blog))


