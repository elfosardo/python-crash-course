"""Defines URL patterns for learning_logs."""

from django.urls import path
from django.contrib.auth.views import login

from . import views


urlpatterns = [
    # Login page
    path('login/', login, {'template_name': 'users/login.html'}, name='login'),
    # Logout Page
    path('logout/', views.logout_view, name='logout'),
    # Registration Page
    path('register/', views.register, name='register'),
    ]
