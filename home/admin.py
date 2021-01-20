from django.contrib import admin
from .models import *
from .models import Write_about_us
from .models import Home_Contact_Booking
class Home_section_2_card_inline(admin.TabularInline):
    model = Home_section_2_card
class Home_setion_2_admin(admin.ModelAdmin):
    inlines = [
        Home_section_2_card_inline
    ]
#######################################
class Manage_service_inline(admin.TabularInline):
    model = Service_text

class Manage_service_admin(admin.ModelAdmin):
    inlines = [
        Manage_service_inline
    ]
#######################################
class Why_Choose_us_inline(admin.TabularInline):
    model = Why_Choose_us_text

class Why_Choose_us_admin(admin.ModelAdmin):
    inlines = [
        Why_Choose_us_inline
    ]
#######################################
class Our_client_inline(admin.TabularInline):
    model = Client_detail

class Our_client_admin(admin.ModelAdmin):
    inlines = [
        Our_client_inline
    ]
#######################################
class Home_section_last_inline(admin.TabularInline):
    model = Home_section_last_text

class Home_section_last_admin(admin.ModelAdmin):
    inlines = [
        Home_section_last_inline
    ]
#######################################
class About_us_section_text(admin.TabularInline):
    model = About_us_section

class About_us_admin(admin.ModelAdmin):
    inlines = [
        About_us_section_text
    ]
#######################################

# Register your models here.
admin.site.register(Home_Contact_Booking)
admin.site.register(Home_section_1)
admin.site.register(Home_section_2,Home_setion_2_admin)
admin.site.register(Home_section_last,Home_section_last_admin)
admin.site.register(Manage_service,Manage_service_admin)
admin.site.register(Why_Choose_us,Why_Choose_us_admin)
admin.site.register(Our_client,Our_client_admin)
admin.site.register(About_us,About_us_admin)
admin.site.register(Contact_us)
admin.site.register(Blog)
admin.site.register(Write_about_us)
admin.site.register(FAQ)
admin.site.register(Home_Contact_Booking_contents)


admin.site.site_title = "GearUpLead"
admin.site.site_header = "GearUpLead Administrative"
# admin.site.index_title = "GearUpLead"