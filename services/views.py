from django.shortcuts import render,HttpResponse
from .models import Service
# Create your views here.
from home.models import Our_client

def services(request):
    section5 = Our_client.objects.first()
    
    return render(request,'service.html',{
        "service" : Service.objects.first(),
        "section5" : section5
    })