from django.contrib import admin
from core.models import ContactUs, Prediction

# Register your models here.
@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['email', 'wallet']

@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'created_at']
    search_fields = ('title', 'content')
