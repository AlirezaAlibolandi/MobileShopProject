from django.db import models
from autoslug import AutoSlugField


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name', unique=True, always_update=True)

class Company(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='company/')

class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name', unique=True, always_update=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.IntegerField()
    stock = models.IntegerField()
    short_description = models.CharField(max_length=300)
    description = models.TextField()
    weight = models.FloatField()
    size = models.CharField(max_length=20)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='products')
    def __str__(self):
        return self.title

class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='Product-images/')
    alt_text = models.CharField(max_length=150)

