from django.contrib import admin
from .models import Artiste, Song, Lyric
# Register your models here.

@admin.register(Artiste)
class ArtisteAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "age")


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ("title", "date_released", "likes", "artiste")


@admin.register(Lyric)
class LyricAdmin(admin.ModelAdmin):
    list_display = ("content", "song")