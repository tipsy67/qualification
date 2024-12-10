from optics.apps import OpticsConfig
from django.urls import path

from optics.views import mainpage

app_name = OpticsConfig.name

urlpatterns = [
    path('', mainpage, name='home'),
]