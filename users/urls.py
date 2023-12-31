from django.urls import path
from . import views


app_name = 'users'

urlpatterns = [
    path('register/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
]
