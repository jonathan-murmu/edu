# Generated by Django 2.1 on 2018-08-05 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course_is_available'),
        ('accounts', '0002_auto_20180805_0623'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='course',
            field=models.ManyToManyField(to='course.Course'),
        ),
    ]