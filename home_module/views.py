from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View

from shop_module.models import Company
from blog_module.models import Article
from .forms import EmailSubscriberForm, ContactUsForm


# Create your views here.
def index(request):
    articles = Article.objects.all()[:3]
    context = {
        'articles': articles
    }
    return render(request, 'home_module/index-page.html', context)


def site_header_component(request):
    brands = Company.objects.all()
    context = {
        'brands': brands
    }
    return render(request, 'shared/site_header_component.html', context)


def site_footer_component(request):
    subscribe_form = EmailSubscriberForm()
    context = {
        'subscribe_form': subscribe_form
    }
    return render(request, 'shared/site_footer_component.html', context)


class EmailSubscriberFormView(View):
    def post(self, request):
        form = EmailSubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(f"Subscribed with {form.cleaned_data['email']}")
        else:
            if 'email' in form.errors:
                email = request.POST.get('email', '')
                return HttpResponse(f'{email} ,This email has already been registered')
            return HttpResponse("An error occurred, please try again.")


class contactUsFormView(View):
    def post(self, request):
        form = ContactUsForm(request.POST)
        if form.is_valid():
            ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
            if ip_address:
                ip_address = ip_address.split(',')[0]
            else:
                ip_address = request.META.get('REMOTE_ADDR', '')
            form.instance.ip_address = ip_address
            form.save()
            return HttpResponse("Thank you for registering")

    def get(self, request):
        form = ContactUsForm()
        context = {
            'form': form
        }
        return render(request, 'home_module/contact-page.html', context)
