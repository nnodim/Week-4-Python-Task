from re import A
from django.contrib import admin
from .models import Artiste, Song, Lyric
# Register your models here.

@admin.register(Artiste)
class ArtisteAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "age")
admin.site.register(Song)
admin.site.register(Lyric)