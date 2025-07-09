from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from core.models import ContactUs, Prediction
from django.shortcuts import get_object_or_404
from django.urls import reverse

# url = reverse('prediction_detail', args=[1])
# Create your views here.
def Home(request):
    predictions = Prediction.objects.all()
    return render(request, 'parent.html', {'predictions': predictions})

def prediction_detail(request, id):
    prediction = get_object_or_404(Prediction, id=id)
    context = {
        'prediction': prediction,
        'id':id,
    }
    return render(request, 'prediction_detail.html', context)

def AjaxContact(request):
    email = request.GET['email']
    wallet = request.GET['wallet']

    contact = ContactUs.objects.create(
        email = email,
        wallet = wallet,
    )

    context = {
        'bool': True,
        'message': 'We are glad to be in touch with you. Thanks for submitting'
    }

    return JsonResponse({'context': context})

