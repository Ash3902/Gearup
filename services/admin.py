from django.contrib import admin
from .models import Service,ServiceSection
# Register your models here.

class ServiceSectionInline(admin.TabularInline):
    model = ServiceSection

class SeriveAdmin(admin.ModelAdmin):
    inlines = [
        ServiceSectionInline
    ]

admin.site.register(Service,SeriveAdmin)