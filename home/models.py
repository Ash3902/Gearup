from django.db import models
from tinymce import HTMLField
from django.template.defaultfilters import slugify
# Create your models here.
class Home_setion_1(models.Model):
    heading = models.CharField(max_length=50)
    sub_heading = models.CharField(max_length=100)
    background_image = models.FileField(upload_to="home/",null=True,blank=True)

class Home_setion_2(models.Model):
    heading = models.CharField(max_length=50)

class Home_setion_2_card(models.Model):
    section_2 = models.ForeignKey(Home_setion_2,on_delete=models.CASCADE)
    image = models.FileField(upload_to="icon/")
    title = models.CharField(max_length=10)
    description = models.TextField()

class Manage_service(models.Model):
    service_name = models.CharField(max_length=20)
    service_price_text = models.CharField(max_length=20)

class Service_text(models.Model):
    service = models.ForeignKey(Manage_service,on_delete=models.CASCADE)
    text = models.CharField(max_length=60)

class Why_Choose_us(models.Model):
    heading = models.CharField(max_length=50)
    sub_heading = models.CharField(max_length=100)
    url = models.URLField(blank=True)
    
class Why_Choose_us_text(models.Model):
    us = models.ForeignKey(Why_Choose_us,on_delete=models.CASCADE)
    text = models.CharField(max_length=90)
    
class Our_client(models.Model):
    heading = models.CharField(max_length=50)

class Client_detail(models.Model):
    client = models.ForeignKey(Our_client,on_delete=models.CASCADE)
    client_name = models.CharField(max_length=90)
    client_image = models.FileField(upload_to="client/")


class Home_section_last(models.Model):
    heading = models.CharField(max_length=50)
    sub_heading = models.CharField(max_length=50)
    image = models.FileField(upload_to="home")

class Home_section_last_text(models.Model):
    last_section = models.ForeignKey(Home_section_last,on_delete=models.CASCADE)
    text = models.CharField(max_length=90)
    
class Contact_us(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    number = models.CharField(max_length=15)
    message = models.TextField()


class Blog(models.Model):
    heading = models.CharField(max_length=200,help_text="maximun, 200 words")
    author_name = models.CharField(max_length=30,help_text="maximum 30 words") 
    date = models.DateTimeField(auto_now=True,editable=False) 
    description = HTMLField()
    meta_description = models.TextField(help_text="Minimum 100 Words",)
    add_to_feature_post = models.BooleanField(default=False) #done
    publish_now = models.BooleanField(default=True) 

    slug = models.SlugField(null=True,blank=True,editable=False)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.heading)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.heading

