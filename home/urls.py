from django.urls import path,include
from django.views.generic import TemplateView
from . import views
urlpatterns = [
    path("",views.index),
    path("contact-us",views.contact,name="contact-us"),
    path("about-us",views.about_us,name="about-us"),
    path("blog",views.BlogList.as_view(),name="blog"),
    path("<int:pk>/<slug>",views.blog_view,name="blog-detail"),
]

            