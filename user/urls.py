from django.urls import path, include
from . import views

app_name = 'user'

urlpatterns = [
    path('signup/', views.signupuser, name='signupuser'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logoutuser/', views.logoutuser, name="logoutuser"),
]
