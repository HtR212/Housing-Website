from django.contrib import admin
from .models import StudentHousing, Review, User, UserReview

# Register your models here.
admin.site.register(StudentHousing)
admin.site.register(Review)
admin.site.register(User)
admin.site.register(UserReview)
