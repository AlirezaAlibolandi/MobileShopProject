from django.urls import path
from . import views
app_name = 'shop'

urlpatterns = [
    path('<slug:slug>', views.ProductDetailView.as_view(), name='detail'),
    path('', views.ProductListView.as_view(), name='shop'),
]