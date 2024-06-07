from django.views.generic import ListView, DetailView

from .models import Product, Category


# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = 'shop_module/shop-page.html'
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.filter(is_active=True).all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['products'] = Product.objects.filter(is_active=True).all()
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop_module/shop-detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recommended_articles'] = Product.objects.exclude(slug=self.object.slug).order_by('?')[:4]
        print(context)
        return context
