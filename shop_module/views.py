from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product


# Create your views here.
class ProductListView(ListView):
    pass

class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop_module/shop-detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'