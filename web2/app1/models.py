from django.db import models

# Create your models here.
class message(models.Model):
    sender = models.CharField(max_length=50,blank=True,null=True,default=0)
    receiver = models.CharField(max_length=50,blank=True,null=True,default=0)
    mes1 = models.CharField(max_length=50,blank=True,null=True,)
    mes2 = models.CharField(max_length=50,blank=True,null=True,)
    mes3 = models.CharField(max_length=50,blank=True,null=True,)
    mes4 = models.CharField(max_length=50,blank=True,null=True,)
