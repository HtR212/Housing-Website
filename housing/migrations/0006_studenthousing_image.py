# Generated by Django 3.2.8 on 2021-10-31 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0005_auto_20211029_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='studenthousing',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
