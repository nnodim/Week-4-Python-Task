from django.db import models
from datetime import datetime

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name

class Song(models.Model):
    title = models.CharField(max_length=400)
    date_released = models.DateField(default=datetime.now)
    likes = models.CharField(max_length=400)
    artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class Lyric(models.Model):
    content = models.CharField(max_length=400)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content