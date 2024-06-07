from django.shortcuts import render
from rest_framework import generics
from shop_module.models import Product
from blog_module.models import Article
from .serializers import ProductSerializer , BlogSerializer
from rest_framework.pagination import PageNumberPagination
# Create your views here.

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10

class ProductGenericAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPageNumberPagination

class BlogtGenericAPIView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = BlogSerializer
    pagination_class = CustomPageNumberPagination
