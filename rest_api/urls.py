from django.urls import path
from . import views
app_name = 'rest_api'
urlpatterns = [
    path('', views.ProductGenericAPIView.as_view(), name='product-list'),
]