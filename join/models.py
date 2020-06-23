from django.utils import timezone
from django.db import models
import datetime
from django.contrib.auth.models import User


# Create your models here.

class Join(models.Model):
    email=models.EmailField()
    first_name=models.CharField(max_length=120,blank=True,null=True)
    last_name=models.CharField(max_length=150,null=True,blank=True)
    zip_code=models.IntegerField()
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)

    def __str__(self):
        return self.email
    
class Subcriber(models.Model):
    email=models.EmailField(null=False,blank=False,unique=True)
    referrer=models.ForeignKey('self',related_name='referrals',on_delete=models.CASCADE,null=True,blank=True)
    ref_id=models.CharField(max_length=120,unique=True)
    ip_address=models.GenericIPAddressField(null=True,blank=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
    


States=[
    ('Tashkent','Tash'),
    ('Samarkand','Sam'),
    ('Bukhara','Bukh'),
    ('Jizzakh',"Jiz"),
]
class Address(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    username=models.CharField(max_length=250)
    password=models.CharField(max_length=250)
    address=models.CharField(max_length=250,null=True,blank=True)
    address2=models.CharField(max_length=250)
    city=models.CharField(max_length=120)
    state=models.CharField(max_length=120,choices=States)
    zip_code=models.PositiveIntegerField()
    remember=models.BooleanField(default=False)


    def __str__(self):
        return self.username
