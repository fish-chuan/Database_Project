from django.contrib import admin
from .models import Ablum, Song, Artist, LikeSong

# Register your models here.

admin.site.register(Ablum)
admin.site.register(Song)
admin.site.register(Artist)
admin.site.register(LikeSong)