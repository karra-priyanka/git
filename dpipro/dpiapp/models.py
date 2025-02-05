from django.db import models

class CourseData(models.Model):
    course_id=models.IntegerField(default=None)
    course_name=models.CharField(max_length=30)
    course_fee=models.IntegerField(default=None)
    course_duration=models.CharField(max_length=40)
    course_startdate=models.DateField(max_length=50)
    course_enddate=models.DateField(max_length=50)
    course_time=models.TimeField(max_length=50)
    institute_name=models.CharField(max_length=60)
    institute_location=models.CharField(max_length=50)
    trainer_name=models.CharField(max_length=60)

class Feedback(models.Model):
    feedback_data=models.CharField(max_length=500)

