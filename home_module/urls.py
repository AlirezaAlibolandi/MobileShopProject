from django.urls import path
from . import views
app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact-us', views.contactUsFormView.as_view(), name='contact-us'),
    path('submitemailform', views.EmailSubscriberFormView.as_view(), name='EmailSubmitform'),
]