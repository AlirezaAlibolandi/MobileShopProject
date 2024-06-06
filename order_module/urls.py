from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('add-to-order', views.add_product_to_order, name='add-product-to-order'),
    path('remove-order-detail', views.remove_order_detail, name='remove_order_detail_ajax'),
    path('change-order-detail', views.change_order_detail_count, name='change_order_detail_ajax'),
    path('cart', views.user_cart, name='cart'),
]
