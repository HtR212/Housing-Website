from django.contrib import admin
from .models import StudentHousing, Review, WebUser, UserReview, SuggestedListings

# Register your models here.
admin.site.register(StudentHousing)
admin.site.register(Review)
admin.site.register(WebUser)
admin.site.register(UserReview)
admin.site.register(SuggestedListings)
