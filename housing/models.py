from django.db import models

# Create your models here.
class StudentHousing(models.Model):
    name = models.CharField(max_length=200)
    distToGrounds = models.FloatField(default=0)
    parking = models.BooleanField()
    cost = models.IntegerField(default=0)
    noiseLevel = models.IntegerField(default=0)

    def __str__(self):
        return self.name

