# Generated by Django 2.1 on 2018-08-05 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180805_0701'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('username',)},
        ),
    ]
