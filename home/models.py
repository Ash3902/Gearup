from django.db import models

# Create your models here.
class Contact_us(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    number = models.CharField(max_length=15)
    message = models.TextField()

