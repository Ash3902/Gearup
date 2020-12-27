from django.urls import path,include
from django.views.generic import TemplateView
urlpatterns = [
    path("",TemplateView.as_view(template_name="home.html")),
    path("contact-us/",TemplateView.as_view(template_name="contact-us.html"),name="contact-us"),
    path("about-us/",TemplateView.as_view(template_name="about-us.html"),name="about-us")
]
