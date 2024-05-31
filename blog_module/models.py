from django.contrib.auth.models import User
from django.db import models
from autoslug import AutoSlugField
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title', unique=True, always_update=True)

class Tag(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title', unique=True, always_update=True)

class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='title', unique=True, always_update=True)
    description = models.TextField()
    short_description = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to='articles/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
