# Generated by Django 2.1 on 2018-08-05 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]
