# Generated by Django 3.2.8 on 2021-11-28 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0018_studenthousingphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='studenthousing',
            name='test',
            field=models.TextField(max_length=200, null=True),
        ),
    ]