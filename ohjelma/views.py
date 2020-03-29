from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from ohjelma.models import Song
from ohjelma.models import Track

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def index(request):
    return HttpResponse('Welcome.')

class SongList(ListView):
    model = Song

class SongView(DetailView):
    model = Song

class SongCreate(CreateView):
    model = Song
    fields = ['song_name', 'song_artist', 'release_year']
    success_url = reverse_lazy('song_list')

class SongUpdate(UpdateView):
    model = Song
    fields = ['song_name', 'song_artist', 'release_year']
    success_url = reverse_lazy('song_list')

class SongDelete(DeleteView):
    model = Song
    success_url = reverse_lazy('song_list')

def TrackView(request):

    Track.objects.all().delete()        #Clear old info

    #Spotify developer keys
    cid = '8f91d5aff7b54e1e93daa49f123d9ee9'
    secret = 'f23421ee54b144cabeab9e2dbe9104a7'

    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
 
    for i in range(0,100,50):
        track_results = sp.search(q='genre:rock', type='track', limit=50,offset=i)
        for i, t in enumerate(track_results['tracks']['items']):

            artist = t['artists'][0]['name']
            song = t['name']
            dur_ms = t['duration_ms']
            pop = t['popularity']

            #Formatting the duration time
            dur_s = (dur_ms/1000)%60
            dur_s = int(dur_s)
            if dur_s < 10:
                dur_s = "0{}".format(dur_s)
            dur_m = (dur_ms/(1000*60))%60
            dur_m = int(dur_m)
            dur = "{}:{}".format(dur_m, dur_s)

            Track.objects.create(track_artist = artist, track_name = song, track_duration = dur, track_popularity = pop)

    alltracks = Track.objects.all()
    context = {'alltracks': alltracks}
        
    return render(request, 'tracks.html', context)
