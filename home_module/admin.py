from django.contrib import admin
from .models import ContactUs,EmailSubscriber
# Register your models here.

admin.site.register(ContactUs)
admin.site.register(EmailSubscriber)