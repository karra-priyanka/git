# Generated by Django 5.1 on 2024-09-01 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpiapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_data', models.CharField(max_length=100)),
            ],
        ),
    ]
