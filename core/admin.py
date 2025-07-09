from django.contrib import admin
from core.models import ContactUs, Prediction

# Register your models here.

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['email', 'wallet']


class PredictionAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'created_at']
    search_fields = ('title', 'content')

admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(Prediction, PredictionAdmin)