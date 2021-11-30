from django.db import models
import geocoder

# Create your models here.
class StudentHousing(models.Model):
    name = models.CharField(max_length=200)
    distToGrounds = models.FloatField(default=0)
    parking = models.BooleanField()
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
    lat = models.FloatField(blank=True, null=True) #leave blank
    long = models.FloatField(blank=True, null=True) #leave blank

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key='pk.eyJ1IjoiYXZhbmVlbnAiLCJhIjoiY2t2bnprNGxhMWs1MTJubzB5M2J0OG95eiJ9.xN5gncTvjcamL4-60POirQ')
        g = g.latlng #[lat, long]
        self.lat = g[0]
        self.long = g[1]
        return super(StudentHousing, self).save(*args, **kwargs)

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

    def valid_parameters(self):
        if 5 >= self.rating >= 0:
            return True
        else:
            return False


class User(models.Model):
    email = models.CharField(max_length=320, primary_key=True) # According to Google, the longest email address could have 320 characters
    gender = models.CharField(max_length=20, default="")
    userName = models.CharField(max_length=100, default="")
    age = models.IntegerField(default=0)
    schoolYear = models.CharField(max_length=50, default="")
    major = models.CharField(max_length=50, default="")

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


class SuggestedListings(models.Model):
    listingName = models.CharField(max_length=200)
    listingAddress = models.CharField(max_length=500)

    def __str__(self):
        return self.listingName

    def valid_parameters(self):
        if len(self.listingName) > 0 and len(self.listingAddress) > 0:
            return True
        else:
            return False


