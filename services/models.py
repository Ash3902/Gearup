from django.db import models
from tinymce.models import HTMLField
# from tinymce import TinyMCE
class Service(models.Model):
    heading = models.CharField(max_length=100)
    sub_heading = models.CharField(max_length=100)

    def __str__(self):
        return self.heading

class ServiceSection(models.Model):
    parent = models.ForeignKey(Service,on_delete=models.CASCADE)
    heading = models.CharField(max_length=100)
    content = HTMLField()
    image = models.FileField(upload_to="service/")
    