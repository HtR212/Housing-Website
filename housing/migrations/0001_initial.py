# Generated by Django 3.2.7 on 2021-10-25 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentHousing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('distToGrounds', models.IntegerField(default=0)),
                ('parking', models.BooleanField()),
                ('cost', models.IntegerField(default=0)),
                ('noiseLevel', models.IntegerField(default=0)),
            ],
        ),
    ]
