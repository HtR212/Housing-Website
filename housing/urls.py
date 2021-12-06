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
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),
    path('profile/submit/', views.submit_profile_view, name='submit_profile'),
    path('manage_reviews/delete/<int:review_id>/<int:housing_id>', views.review_delete, name='review_delete'),
    path('manage_reviews/edit/<int:review_id>/', views.review_edit, name='review_edit'),
    path('manage_reviews/edit/<int:review_id>/submit/<int:housing_id>', views.review_edit_submit, name='review_edit_submit'),
]