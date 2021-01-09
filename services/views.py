from django.shortcuts import render,HttpResponse
from .models import Service
# Create your views here.
from home.models import Our_client

def services(request):
    section5 = Our_client.objects.first()
    services = Service.objects.filter(is_core=False)
    return render(request,'service.html',{
        "service" : services[0] if services else None,
        "section5" : section5
    })
def core_services(request):
    section5 = Our_client.objects.first()
    services = Service.objects.filter(is_core=True)
    
    return render(request,'service.html',{
        "service" : services[0] if services else None,
        "section5" : section5
    })