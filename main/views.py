from django.shortcuts import render
from .models import Ablum, Song
# Create your views here.

def home(request):
    lists = Ablum.objects.all()
    return render(request, 'home.html', {'data':lists})

def song_list(request, ablumId):
    ablumInfo = Ablum.objects.filter(id=ablumId)
    songData = Song.objects.filter(ablum_name_id=ablumId)
    return render(request, 'song_list.html', {'ablumInfo':ablumInfo, 'songData':songData})
