from django.contrib import admin
from .models import studentdata
# Register your models here.

class StudentData(admin.ModelAdmin):
    list_display =('first_name','last_name','id')

admin.site.register(studentdata,StudentData)