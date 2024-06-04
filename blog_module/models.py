from django.contrib.auth.models import User
from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
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
    short_description = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to='articles/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:article_detail',args=[self.slug])
