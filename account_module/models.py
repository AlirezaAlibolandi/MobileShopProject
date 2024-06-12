from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_information')
    birth_date = models.DateField(blank=True, null=True,verbose_name='تاریخ تولد')
    phone_number = models.CharField(max_length=20, blank=True, null=True,verbose_name='تلفن همراه')
    address = models.CharField(max_length=100, blank=True, null=True,verbose_name='آدرس')
    image = models.ImageField(upload_to='profile/', blank=True, null=True,verbose_name='تصویر پروفایل')

    def __str__(self):
        return self.user.username
