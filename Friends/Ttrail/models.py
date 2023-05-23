from django.db import models

# Create your models here.
class Call_Back(models.Model):
    Name = models.CharField(max_length=100,null=True,Blank=True)
    Email = models.CharField(max_length=100,null=True,Blank=True)
    Call_date = models.CharField(max_length=100,null=True,Blank=True)
    Call_time = models.CharField(max_length=100,null=True,Blank=True)
    Message = models.TextField()
    date = models.DateField(auto_now=True)

class Newsletter(models.Model):
    Email = models.CharField(max_length=100,null=True,Blank=True)
    date = models.DateField(auto_now=True)