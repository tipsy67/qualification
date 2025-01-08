from django.test import TestCase, Client
from django.urls import reverse

from blog.models import Blog
from blog.templatetags.blog_tags import add_media


class BlogAppTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.blog = Blog.objects.create(title='Blog for test')
        content = ['123456790'+str(i) for i in range(15)]
        content = ''.join(content)
        cls.blog.content = content
        cls.blog.save()
        cls.client = Client()


    def test_blog_model(self):
        blog=Blog.objects.get(id=self.blog.pk)

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


    def test_short_content(self):
        blog=Blog.objects.get(id=self.blog.pk)

        self.assertGreater(len(blog.content), 100)
        self.assertEqual(len(blog.short_content), 100)


    def test_views_BlogListView(self):
        url = reverse('blog:blog_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_list.html')


    def test_views_BlogDetailView(self):
        url = reverse('blog:blog_detail', args=[self.blog.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_detail.html')

    def test_blog_tags(self):
        self.assertEqual(add_media(None), "#")
        self.assertEqual(add_media("test.img"), "/media/test.img")
