from django.db import models

class FakeData(models.Model) :
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=125)
    company = models.CharField(max_length=225)
    location = models.CharField(max_length= 225, default= None)
    salary = models.IntegerField(default=None)
    emp_id = models.IntegerField(default=None)
    address = models.CharField(max_length=225)

