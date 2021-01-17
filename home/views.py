from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from .models import (
    Contact_us,
    Blog,
    Home_section_1,
    Home_section_2,
    Home_section_last,
    Why_Choose_us,
    Our_client,
    Manage_service,
    About_us,
    Write_about_us,
    FAQ,
    Home_Contact_Booking
)
from django.views.generic import ListView
from django.contrib import messages

from careers.models import Career
# Create your views here.
def index(request):
    section1 = Home_section_1.objects.first()
    section2 = Home_section_2.objects.first()
    section3 = Manage_service.objects.all()[:3]
    section4 = Why_Choose_us.objects.first()
    section5 = Our_client.objects.first()
    section6 = Home_section_last.objects.first()
    faqs = FAQ.objects.all()
    # print(section1.heading)

    
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        number = request.POST["number"]
        message = request.POST["message"]
        print(type(number))
        Home_Contact_Booking.objects.create(name=name,email=email,number=number,message=message).save()
        messages.success(request,'Your message is saved please do not submit again withen 24 hour Our Company Contact You !')
        return redirect("home")





    return render(request,"home.html",{
        "section1" : section1,
        "section2" : section2,
        "section3" : section3,
        "section4" : section4,
        "section5" : section5,
        "section6" : section6,
        "faqs" : faqs,
    })

class BlogList(ListView):
    queryset = Blog.objects.filter(publish_now=True).exclude(add_to_feature_post=True)
    template_name = "blog.html"
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        featured_blog = Blog.objects.filter(add_to_feature_post=True).order_by("-id")[:3]
        # print(featured_blog)
        context['featured_blog'] = featured_blog
        return context
def blog_view(request,pk,slug):
    blog = Blog.objects.get(id=pk)

    return render(request,"blog-detail.html",{"blog":blog})

def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        number = request.POST["number"]
        message = request.POST["message"]
        print(type(number))
        Contact_us.objects.create(name=name,email=email,number=number,message=message).save()
        messages.success(request,'Your message is saved please do not submit again withen 24 hour contact you !')
        return redirect("contact-us")
    return render(request,"contact-us.html")

def about_us(request):
    about = About_us.objects.first()
    return render(request,"about-us.html",{
        'about':about
    })


def write_for_us(request):
    
    write_data = Write_about_us.objects.filter(show=True)
    
    if request.method == 'POST':
        first_name =  request.POST['first_name']
        last_name =  request.POST['last_name']
        
        image =  request.FILES['image']
        description = request.POST['description']
        messages.success(request,'Your feedback is saved please do not submit again')
        fs = FileSystemStorage()
        myfile = fs.save("write_us/" +image.name , image)
        
        # print(fs.url(myfile))

        write_us = Write_about_us(first_name=first_name,last_name=last_name,image="write_us/" +image.name, description=description)
        write_us.save()
        return redirect("write_for_us")

    return render(request,'write-for-us.html',{'write_data':write_data})



def job_opening(request):
    return render(request,'job-opening.html',{
        "careers": Career.objects.all()
    })


def referral_program(request):
    return render(request,'referral-program.html')