# Generated by Django 3.2.8 on 2021-10-29 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0004_auto_20211029_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='studenthousing',
            name='address',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='studenthousing',
            name='averageRating',
            field=models.IntegerField(default=0),
        ),
    ]
