from django.urls import path, include
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('feed', views.feed, name="feed"),
]
