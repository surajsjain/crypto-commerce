# Generated by Django 3.1 on 2020-08-12 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userstats', '0003_auto_20200812_1141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userstat',
            name='city',
        ),
    ]
