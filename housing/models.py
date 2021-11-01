from django.db import models


# Create your models here.
class StudentHousing(models.Model):
    name = models.CharField(max_length=200)
    distToGrounds = models.FloatField(default=0)
    parking = models.BooleanField()
    # cost = models.IntegerField(default=0)
    # noiseLevel = models.IntegerField(default=0)
    minCost = models.IntegerField(default=0)
    maxCost = models.IntegerField(default=0)
    location = models.TextField(max_length=200, null=True)
    landlordEmail = models.CharField(max_length=200, null=True)
    landlordPhone = models.CharField(max_length=200, null=True)
    amenities = models.TextField(max_length=200, null=True)
    deadline = models.CharField(max_length=200, null=True)
    averageRating = models.IntegerField(default=0)
    address = models.TextField(max_length=200, null=True)

    def __str__(self):
        return self.name

    def valid_parameters(self):
        if self.distToGrounds > 0 and self.minCost > 0 and self.maxCost > 0 and self.averageRating >= 0 and self.averageRating <= 5:
            return True
        else:
            return False
 