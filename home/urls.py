from django.urls import path,include
from django.views.generic import TemplateView
from . import views
urlpatterns = [
    path("",TemplateView.as_view(template_name="home.html")),
    path("contact-us",views.contact,name="contact-us"),
    path("about-us",TemplateView.as_view(template_name="about-us.html"),name="about-us"),
    path("blog",views.BlogList.as_view(),name="blog"),
    path("<int:pk>/<slug>",views.blog_view,name="blog-detail"),
]

            