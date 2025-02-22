# Generated by Django 5.1 on 2024-09-01 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.IntegerField(default=None)),
                ('course_name', models.CharField(max_length=30)),
                ('course_fee', models.IntegerField(default=None)),
                ('course_duration', models.CharField(max_length=40)),
                ('course_startdate', models.DateField(max_length=50)),
                ('course_enddate', models.DateField(max_length=50)),
                ('course_time', models.TimeField(max_length=50)),
                ('institute_name', models.CharField(max_length=60)),
                ('institute_location', models.CharField(max_length=50)),
                ('trainer_name', models.CharField(max_length=60)),
            ],
        ),
    ]
