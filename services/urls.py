from django.urls import path,include
from django.views.generic import TemplateView
from . import views
urlpatterns = [
    path("",views.services,name="services"),
    path("core",views.core_services,name="core_services"),
]