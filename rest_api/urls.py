from django.urls import path
from . import views
app_name = 'rest_api'
urlpatterns = [
    path('shop', views.ProductGenericAPIView.as_view(), name='product-list'),
    path('blog', views.BlogtGenericAPIView.as_view(), name='blog-list'),
]