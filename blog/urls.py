from django.urls import path
from django.views.decorators.cache import cache_page

from blog.apps import BlogConfig
from blog.views import (BlogCreateView, BlogDeleteView, BlogDetailView,
                        BlogListView, BlogUpdateView)

appname = BlogConfig.name

urlpatterns = [
   path ('blog/', BlogListView.as_view(),name='blog_list'),
   path('view_blog/<slug:slug>', BlogDetailView.as_view(), name='blog_detail'),
]