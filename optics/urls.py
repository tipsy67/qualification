from optics.apps import OpticsConfig
from django.urls import path

from optics.views import mainpage, FeedbackCreateView, thank_you, about, \
    product_list_view, ServiceListView

app_name = OpticsConfig.name

urlpatterns = [
    path('', mainpage, name='home'),
    path('contact/', FeedbackCreateView.as_view(), name='contact'),
    path('thank-you/', thank_you, name='thank-you'),
    path('about/', about, name='about'),
    path('shop-list/', product_list_view, name='shop-list'),
    path('service-list/', ServiceListView.as_view(), name='service-list'),
]