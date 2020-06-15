from django.utils import timezone
from django.db import models
import datetime


# Create your models here.

class Join(models.Model):
    email=models.EmailField()
    first_name=models.CharField(max_length=120,blank=True,null=True)
    last_name=models.CharField(max_length=150,null=True,blank=True)
    zip_code=models.IntegerField()
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)

    def __str__(self):
        return self.email
    
