from django.db import models

# Create your models here.
class indexPage(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    address=models.CharField(max_length=100)
    institute=models.CharField(max_length=50)

