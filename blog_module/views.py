from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Article
# Create your views here.
class BlogListView(ListView):
    model = Article
    template_name = 'blog_module/blog-list.html'
    paginate_by = 6
    queryset = Article.objects.all().filter(is_active=True)

class BlogDetailView(DetailView):
    model = Article
    template_name = 'blog_module/blog-detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'