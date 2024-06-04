from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article, Category,Tag


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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recommended_articles'] = Article.objects.exclude(slug=self.object.slug).order_by('?')[:3]
        print(context)
        return context


def blog_sidebar_component(request):
    category = Category.objects.all()
    article = Article.objects.all().filter(is_active=True)[:3]
    tag = Tag.objects.all()[:6]
    context = {
        'category': category,
        'last_article':article,
        'tags':tag,
    }
    return render(request, 'blog_module/blog-sidebar-component.html', context)
