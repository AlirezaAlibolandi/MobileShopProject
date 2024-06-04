from django.contrib.auth.models import User
from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from slugify import slugify


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    slug = AutoSlugField(populate_from='title', unique=True, always_update=True)

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    slug = AutoSlugField(populate_from='title', unique=True, always_update=True)

    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ ها'

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده')
    slug = AutoSlugField(populate_from='get_slug', unique=True, always_update=True)
    description = models.TextField(verbose_name='توضیحات')
    short_description = models.CharField(max_length=300, verbose_name='توضیحات کوتاه')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='دسته بندی')
    tags = models.ManyToManyField(Tag, verbose_name='تگ ها')
    image = models.ImageField(upload_to='articles/', verbose_name='تصویر مقاله')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False, verbose_name='وضعیت')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def get_slug(self):
        return slugify(self.title, separator='-', lowercase=True, replacements=[(' ', '-')])

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:article_detail', args=[self.slug])
