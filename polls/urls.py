from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.showIntro, name='intro'),
    path('listSongs', views.Songs.as_view(), name='listSongs'),
    path('contacts', views.showContacts, name='contacts'),
]
