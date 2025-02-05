from django.db import models
 
# Create your models here.
class indexpage(models.Model):
    f_name=models.CharField(max_length=50)
    l_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=150)
    address=models.CharField(max_length=150)
