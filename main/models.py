from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Artist(models.Model):
    singer_name = models.CharField(max_length=30)
    total_song = models.IntegerField(default=0)
    singer_img = models.ImageField(upload_to='singerImg')

class Ablum(models.Model):
    ablum_name = models.CharField(max_length=50)
    YEAR_CHOICES = []
    r = 1980
    for r in range(1980, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))
    release_year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    ablum_singer = models.ForeignKey(Artist, related_name='singer', on_delete=models.CASCADE)
    upLoad_user = models.ForeignKey(User, related_name='uploadUser', on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='cover')

class Song(models.Model):
    song_order = models.IntegerField(default=0)
    song_name = models.CharField(max_length=50)
    song_singer = models.CharField(max_length=50)
    song_source = models.FileField(upload_to='source')
    release_year = models.ForeignKey(
        Ablum,
        related_name='year',
        on_delete=models.CASCADE
    )
    ablum_name = models.ForeignKey(
        Ablum,
        related_name='ablum',
        on_delete=models.CASCADE
    )

    Pop = 'Pop'
    J_Pop = 'J-Pop'
    Jazz = 'Jazz'
    Classic = 'Classic'
    Blue = 'Blue'
    EDM = 'EDM'
    Other = 'Other'

    SONG_TYPE = [
        (Pop, 'Pop'),
        (J_Pop, 'J-Pop'),
        (Jazz, 'Jazz'),
        (Classic, 'Classic'),
        (Blue, 'Blue'),
        (EDM, 'EDM'),
        (Other, 'Other')
    ]

    song_type = models.CharField(
        max_length=7,
        choices=SONG_TYPE,
        default=Pop,
    )

    chinese = 'CH'
    japan = 'JP'
    english = 'EN'
    other = 'OTH'

    LANGUAGE_TYPE = [
        (chinese, '中文'),
        (japan, '日文'),
        (english, '英文'),
        (other, '其他'),
    ]

    language_type = models.CharField(
        max_length=2,
        choices=LANGUAGE_TYPE,
        default=chinese
    )

class LikeSong(models.Model):
    username = models.ForeignKey(User, related_name='like_user', on_delete=models.CASCADE)
    is_like = models.BooleanField(default=False)
