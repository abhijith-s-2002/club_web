from django.db import models

# Create your models here.
class gallery(models.Model):
    image=models.ImageField(upload_to='images/')
    
class images(models.Model):
    image=models.ImageField(upload_to='images/')
    about=models.CharField(max_length=1000)
class event(models.Model):
    event_name=models.CharField(max_length=100)
    description=models.CharField(max_length=1000000)
    price=models.CharField(max_length=100)
    pic=models.ImageField(upload_to='images/')
class Registration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    year = models.IntegerField()
    event = models.CharField(max_length=50)
    comments = models.TextField(blank=True, null=True)