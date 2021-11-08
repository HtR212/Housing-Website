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
    averageRating = models.FloatField(default=0)
    address = models.TextField(max_length=200, null=True)
    image = models.ImageField(blank=True, null=True) #makes it optional to include an image

    def __str__(self):
        return self.name

    def valid_parameters(self):
        if self.distToGrounds > 0 and self.minCost > 0 and self.maxCost > 0 and self.averageRating >= 0 and self.averageRating <= 5:
            return True
        else:
            return False


class Review(models.Model):
    house = models.ForeignKey(StudentHousing, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    comment = models.TextField(max_length=200, default="")
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return str(self.pub_date)+' '+str(self.rating)+' '+self.comment[:10]


class User(models.Model):
    email = models.CharField(max_length=320, primary_key=True) # According to Google, the longest email address could have 320 characters

    def __str__(self):
        return self.email


class UserReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_id = models.IntegerField(default=0)

    def __str__(self):
        return str(self.review_id)


class UserFavorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    favorite_housing_id = models.IntegerField(default=0)

    def __str__(self):
        return str(self.favorite_housing_id)
