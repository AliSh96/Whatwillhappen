from django.urls import path
from core.views import *

app_name = 'core'

urlpatterns = [
    path('', Home, name='Home'),
    path('ajax-contact-form/', AjaxContact),
    path('prediction/<int:id>/', prediction_detail, name='prediction_detail'),
]