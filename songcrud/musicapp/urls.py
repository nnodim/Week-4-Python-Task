from django.urls import path, include
from .views import SongList, SongDetail, ArtisteList

urlpatterns = [
    path('ArtisteList', ArtisteList.as_view()),
    path('SongList', SongList.as_view()),
    path('SongDetail/<int:pk>/', SongDetail.as_view())
]
