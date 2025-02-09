from django.urls import path

from optics.apps import OpticsConfig
from optics.views import (
    FeedbackCreateView,
    about,
    main_page,
    product_list_view,
    service_detail_view,
    service_list_view,
    thank_you,
)

app_name = OpticsConfig.name

urlpatterns = [
    path('', main_page, name='home'),
    path('contact/', FeedbackCreateView.as_view(), name='contact'),
    path('thank-you/', thank_you, name='thank-you'),
    path('about/', about, name='about'),
    path('shop-list/', product_list_view, name='shop-list'),
    path('service-list/', service_list_view, name='service-list'),
    path('service-detail/<int:pk>/', service_detail_view, name='service-detail'),
]
