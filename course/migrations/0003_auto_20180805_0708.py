# Generated by Django 2.1 on 2018-08-05 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course_is_available'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ('course_name',)},
        ),
    ]
