from django.db import models
from autoslug import AutoSlugField
from slugify import slugify
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    image = models.ImageField(upload_to='category/', verbose_name='تصویر دسته بندی', null=True, blank=True)
    slug = AutoSlugField(populate_from='title', unique=True, always_update=True)

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title


class Company(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام')
    image = models.ImageField(upload_to='company/')

    class Meta:
        verbose_name = 'شرکت'
        verbose_name_plural = 'شرکت ها'

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    slug = AutoSlugField(populate_from='get_slug', unique=True, always_update=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='دسته بندی')
    price = models.IntegerField(verbose_name='قیمت')
    stock = models.IntegerField(verbose_name='تعداد در انبار')
    short_description = models.CharField(max_length=300, verbose_name='توضیحات کوتاه')
    description = models.TextField(verbose_name='توضیحات')
    weight = models.FloatField(verbose_name='وزن')
    size = models.CharField(max_length=20, verbose_name='سایز')
    is_active = models.BooleanField(default=False, verbose_name='وضعیت')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='products', verbose_name='شرکت')

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def get_slug(self):
        return slugify(self.title, separator='-', lowercase=True, replacements=[(' ', '-')])

    def get_absolute_url(self):
        return reverse('shop:detail', args=[self.slug])

    def __str__(self):
        return self.title


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name='محصول')
    image = models.ImageField(upload_to='Product-images/', verbose_name='تصویر')
    alt_text = models.CharField(max_length=150, verbose_name='متن تصویر')

    class Meta:
        verbose_name = 'تصویر'
        verbose_name_plural = 'تصاویر'

    def __str__(self):
        return f'{self.product} - {self.alt_text}'
