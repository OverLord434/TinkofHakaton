from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import LoginUsersView, ProfileView, trainers_redirect, edit_profile, register, home

app_name = 'users'

urlpatterns = [
    path('register/', register, name='register'),
    path('home/', home, name='home'),
    path('login/', LoginUsersView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('trainers_redirect/', trainers_redirect, name='trainers_redirect'),
    path('edit_profile/', edit_profile, name='edit_profile')
]