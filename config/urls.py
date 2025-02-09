from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('optics.urls', namespace='optics')),
    path('', include(('blog.urls', 'blog'), namespace='blog')),
    path('', include(('appointment.urls', 'appointment'), namespace='appointment')),
    path('', include(('users.urls', 'users'), namespace='users')),
    path('', include(('cart.urls', 'cart'), namespace='cart')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
