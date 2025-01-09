from django.views.generic import DetailView, ListView

from blog.models import Blog
from config.settings import MAIN_STREAMER_PATH, BLOG_PER_PAGE


class BlogListView(ListView):
    model = Blog
    paginate_by = BLOG_PER_PAGE

    streamer_content = {'title': 'Наш блог'}
    streamer_path = MAIN_STREAMER_PATH.copy()
    streamer_path.append({'name': 'Статьи', 'url': '#'})
    streamer_content['path'] = streamer_path

    extra_context = {
        'streamer_content': streamer_content,
    }

    def get_queryset(self):
        return Blog.objects.filter(is_published=True)


class BlogDetailView(DetailView):
    model = Blog

    streamer_content = {'title': 'Наш блог'}
    streamer_path = MAIN_STREAMER_PATH.copy()
    streamer_path.append({'name': 'Статьи', 'url': 'blog:blog_list'})
    streamer_content['path'] = streamer_path
    streamer_path.append(
        {
            'name': 'Текущая',
        }
    )
    streamer_content['path'] = streamer_path

    extra_context = {
        'streamer_content': streamer_content,
    }

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        # self.streamer_path = self.streamer_path[:3]
        # self.streamer_path.append({'name' : self.object.title[:12]+'...', })
        self.object.save()

        return self.object
