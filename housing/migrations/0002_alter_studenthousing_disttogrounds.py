# Generated by Django 3.2.7 on 2021-10-27 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studenthousing',
            name='distToGrounds',
            field=models.FloatField(default=0),
        ),
    ]