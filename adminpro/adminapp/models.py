from django.db import models

class studentdata(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=100)
