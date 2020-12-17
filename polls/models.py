from django.contrib.auth.models import User
from django.db import models
import urllib.parse
import social_django


class Song(models.Model):
    album_name = models.CharField(max_length=100, default='')
    name = models.CharField(max_length=10, default='')
    marks = models.IntegerField(default=0)

    def __str__(self):
        return ' '.join([self.album_name, self.name])

    def getMusicLink(self):
        link = 'https://musictestingneuro.s3.eu-central-1.amazonaws.com/media/' + self.name + '.mp3'
        return link


class Mark(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    valence = models.FloatField(default=0)
    arousal = models.FloatField(default=0)

    def __str__(self):
        return 'Song name=' + str(self.song.id) + ';' + 'valence=' + str(self.valence) + ';' + 'arousal=' + str(
            self.arousal)
