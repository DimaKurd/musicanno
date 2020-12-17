from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from .models import *


class Songs(View):

    def get(self, request):
        if request.user.is_authenticated:
            user_marks = Mark.objects.filter(user=request.user)
            user_songs = [mark.song for mark in user_marks]
            all_songs = Song.objects.filter(marks__lt=3)
            songs = list((set(all_songs).difference(set(user_songs))))
            songs = sorted(songs, key=lambda x: str(x.name))

            songs_for_marking = songs[::10][:5]

            return render(request, 'polls/listSong.html', context={'songs': songs_for_marking,
                                                                   'survey': 'active'})
        else:
            return HttpResponseRedirect(reverse('polls:intro'))


    def post(self, request):
        if request.user.is_authenticated:
            for i in range(1, 6):
                song_id = request.POST['song_' + str(i)]
                valence = request.POST['valence_' + str(i)]
                arousal = request.POST['arousal_' + str(i)]

                song = Song.objects.get(pk=song_id)
                song.marks += 1
                song.save()

                new_mark = Mark(song=Song.objects.get(pk=song_id), valence=valence, arousal=arousal, user=request.user)
                new_mark.save()

                request.session['status'] = 'success'
            return HttpResponseRedirect(reverse('polls:intro'))
        else:
            return HttpResponseRedirect(reverse('polls:intro'))




def showIntro(request):
    status = request.session.get('status', 'start')
    request.session['status'] = 'start'
    return render(request, 'polls/Intro.html', {'status': status,
                                                'intro': 'active'})


def showContacts(request):
    return render(request, 'polls/contacts.html', context={'contacts': 'active'})
