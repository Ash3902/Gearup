from django.shortcuts import render,redirect
from .models import Contact_us,Blog,Home_setion_1,Home_setion_2,Home_section_last,Why_Choose_us,Our_client
from django.views.generic import ListView
# Create your views here.
def index(request):
    section1 = Home_setion_1.objects.first()
    print(section1.heading)
    return render(request,"home.html",{
        "section1" : section1
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
        return redirect("contact-us")
    return render(request,"contact-us.html")