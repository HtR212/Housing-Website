from django.contrib import admin
from .models import StudentHousing, Review, User, UserReview, SuggestedListings

# Register your models here.
admin.site.register(StudentHousing)
admin.site.register(Review)
admin.site.register(User)
admin.site.register(UserReview)
admin.site.register(SuggestedListings)

