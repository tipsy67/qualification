
from django.views.generic import (DetailView, ListView,)

from blog.models import Blog
from config.settings import MAIN_STREAMER_PATH


class BlogListView(ListView):
    model = Blog

    streamer_content = {'title' : 'Наш блог'}
    streamer_path = MAIN_STREAMER_PATH.copy()
    streamer_path.append({'name' : 'Статьи', 'url' : '#'})
    streamer_content['path'] = streamer_path

    extra_context = {
        'streamer_content': streamer_content,
    }

    def get_queryset(self):
        return Blog.objects.filter(is_published=True)


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()

        return self.object
