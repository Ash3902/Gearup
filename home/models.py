from django.db import models
from tinymce import HTMLField
from django.template.defaultfilters import slugify
# Create your models here.
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

