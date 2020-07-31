from django.db import models

# Create your models here.
class RouterDetails(models.Model):
   
    id = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=100)
    sapid = models.CharField(max_length=100)
    loopbackid = models.CharField(max_length=100)
    ipv4 = models.CharField(max_length=100)
    mac_address = models.CharField(max_length=100)
    status = models.BooleanField(default=True)