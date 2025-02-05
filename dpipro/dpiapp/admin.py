from django.contrib import admin
from .models import CourseData

class Admin(admin.ModelAdmin):
    list_display='course_id','course_name','course_fee','course_duration','course_startdate','course_enddate','course_time','institute_name','institute_location','trainer_name'
admin.site.register(CourseData,Admin)
