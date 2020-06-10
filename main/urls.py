from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('songList/<int:ablumId>', views.song_list, name="song_list"),
]