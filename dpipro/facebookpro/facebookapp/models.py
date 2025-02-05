from django.db import models

# Create your models here.
class ContactForm(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50) 
    email=models.EmailField(max_length=100)
    number=models.BigIntegerField(default=0)
    iname=models.CharField(max_length=70)
    address=models.CharField(max_length=150)
