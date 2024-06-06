from django.db import models


# Create your models here.
class EmailSubscriber(models.Model):
    email = models.EmailField()

    class Meta:
        verbose_name = 'Email Subscriber'
        verbose_name_plural = 'Email Subscribers'
        db_table = 'email_subscriber'

    def __str__(self):
        return self.email

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return f'{self.name} - {self.email}'
    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'