from django.shortcuts import render
from rest_framework import generics
from shop_module.models import Product
from .serializers import ProductSerializer
from rest_framework.pagination import PageNumberPagination
# Create your views here.

class ProductGenericAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination
    PageNumberPagination.page_size = 50