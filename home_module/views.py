from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'home_module/index-page.html')