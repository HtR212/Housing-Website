from django.urls import path

from . import views
from allauth.account.views import LogoutView

app_name = 'housing'

urlpatterns = [
    path('', views.index, name='index'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('list/', views.HousingListView.as_view(), name='studentHousingList'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:housing_id>/review_submit/', views.review_submit, name='review_submit'),
    path('manage_reviews/', views.user_review_list, name='review_list'),
    path('submission/', views.SuggestionView.as_view(), name='submission'),
    path('submission/success/', views.successful_submission_view, name='success'),
]