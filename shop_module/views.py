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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recommended_articles'] = Product.objects.exclude(slug=self.object.slug).order_by('?')[:3]
        print(context)
        return context