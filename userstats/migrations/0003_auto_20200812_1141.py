# Generated by Django 3.1 on 2020-08-12 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userstats', '0002_auto_20200812_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstat',
            name='google_id',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
    ]