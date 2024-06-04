from django.shortcuts import render
from shop_module.models import Company
from blog_module.models import Article
# Create your views here.
def index(request):
    articles = Article.objects.all()[:3]
    context = {
        'articles':articles
    }
    return render(request,'home_module/index-page.html',context)

def site_header_component(request):
    brands = Company.objects.all()
    context = {
        'brands':brands
    }
    return render(request,'shared/site_header_component.html',context)

def site_footer_component(request):
    context = {
        'text':'text'
    }
    return render(request,'shared/site_footer_component.html',context)