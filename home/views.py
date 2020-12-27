from django.shortcuts import render,redirect
from .models import Contact_us
# Create your views here.
def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        number = request.POST["number"]
        message = request.POST["message"]
        print(type(number))
        Contact_us.objects.create(name=name,email=email,number=number,message=message).save()
        return redirect("contact-us")
    return render(request,"contact-us.html")