from django.db import models

# Create your models here.
class StudentData(models.Models):
    student_name = models.CharField(max_length=50)
    student_id =  models.IntegerField()
    father_name= models.CharField(max_length=50)
    student_phn= models.BigIntegerField(default=0) 