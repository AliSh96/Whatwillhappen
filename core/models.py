from django.db import models

# Create your models here.
class ContactUs(models.Model):
    email = models.CharField(max_length=200)
    wallet = models.CharField(max_length=200)

    class Meta():
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"

    def __str__(self):
        return self.email
    
class Prediction(models.Model):
    title = models.CharField(max_length=200, verbose_name='title')
    content = models.TextField(verbose_name='content')
    image = models.ImageField(upload_to="predictions/", null=True, blank=True, verbose_name="image")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='create at')

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Prediction'
        verbose_name_plural = 'Predictions'