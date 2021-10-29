from django.urls import path

from . import views
from allauth.account.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('logout', LogoutView.as_view()),
]