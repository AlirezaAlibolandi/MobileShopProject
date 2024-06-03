from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'home_module/index-page.html')

def site_header_component(request):
    context = {
        'text':'text'
    }
    return render(request,'shared/site_header_component.html',context)

def site_footer_component(request):
    context = {
        'text':'text'
    }
    return render(request,'shared/site_footer_component.html',context)