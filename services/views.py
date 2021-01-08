from django.shortcuts import render,HttpResponse
from .models import Service
# Create your views here.


def services(request):
    
    return render(request,'service.html',{
        "service" : Service.objects.first()
    })