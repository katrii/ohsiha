from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from ohjelma.models import Song
from ohjelma.models import Track

import json
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


#Formatting the duration time
#Takes milliseconds as parameter and returns a string mm:ss
def MsFormat(milliseconds):
    dur_s = (milliseconds/1000)%60
    dur_s = int(dur_s)
    if dur_s < 10:
        dur_s = "0{}".format(dur_s)
    dur_m = (milliseconds/(1000*60))%60
    dur_m = int(dur_m)
    dur = "{}:{}".format(dur_m, dur_s)

    return dur


def TrackView(request, tracksyear):

    Track.objects.all().delete()        #Clear old info
    query = 'year:{}'.format(tracksyear)

    #Spotify developer keys
    cid = '8f91d5aff7b54e1e93daa49f123d9ee9'
    secret = 'f23421ee54b144cabeab9e2dbe9104a7'

    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

    #Lists for counting year averages
    l_dance = []
    l_en = []
    l_aco = []
    l_val = []
 
    for i in range(0,100,50):
        track_results = sp.search(q=query, type='track', limit=50,offset=i)
        for i, t in enumerate(track_results['tracks']['items']):

            id = t['id']
            artist = t['artists'][0]['name']
            song = t['name']
            dur_ms = t['duration_ms']
            pop = t['popularity']
            dur = MsFormat(dur_ms)

            trackinfo = sp.audio_features(id)
            dance = trackinfo[0]['danceability']
            en = trackinfo[0]['energy']
            key = trackinfo[0]['key']
            loud = trackinfo[0]['loudness']
            spee = trackinfo[0]['speechiness']
            aco = trackinfo[0]['acousticness']
            inst = trackinfo[0]['instrumentalness']
            live = trackinfo[0]['liveness']
            val = trackinfo[0]['valence']
            temp = trackinfo[0]['tempo']

            l_dance.append(dance)
            l_en.append(en)
            l_aco.append(aco)
            l_val.append(val)

            Track.objects.create(track_id = id, track_artist = artist, 
            track_name = song, track_duration = dur, track_popularity = pop, 
            track_danceability = dance, track_energy = en, track_key = key,
            track_loudness = loud, track_speechiness = spee, 
            track_acousticness = aco, track_instrumentalness = inst, 
            track_liveness = live, track_valence = val, track_tempo = temp)

    avgdance = calculate_average(l_dance)*100
    avgene = calculate_average(l_en)*100
    avgaco = calculate_average(l_aco)*100
    avgval = calculate_average(l_val)*100

    alltracks = Track.objects.all()
    context = {'alltracks': alltracks, 'year': tracksyear, 'avgdance': avgdance, 'avgene': avgene, 'avgaco': avgaco, 'avgval': avgval}
        
    return render(request, 'tracks.html', context)

#View for each track detailed information
class Analysis(DetailView):
    model = Track


#Takes a list (of numbers) as parameter, returns the average
def calculate_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t           

    avg = sum_num / len(num)
    return avg


#View for analytics
def YearAnalysis(request):

    #Spotify developer keys
    cid = '8f91d5aff7b54e1e93daa49f123d9ee9'
    secret = 'f23421ee54b144cabeab9e2dbe9104a7'

    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    
    #Lists for saving yearly averages
    dance = []
    en = []
    aco = []
    val = []

    years = []
    most_populars = []

    most_danceable = ""
    best_dance = 0

    happiest = ""
    best_val = 0

    most_acoustic = ""
    best_aco = 0

    most_energetic = ""
    best_en = 0


    for year in range (1980, 2020):

        bestpop = 0
        mostpop = ""

        l_dance = []
        l_en = []
        l_aco = []
        l_val = []

        for i in range(0,100,50):
            query = 'year:{}'.format(year)
            track_results = sp.search(q=query, type='track', limit=50, offset=i)
            for i, t in enumerate(track_results['tracks']['items']):

                #Popularity check
                pop = t['popularity']
                if pop > bestpop:
                    mostpop = "{} by {}. Popularity: {}.".format(t['name'], t['artists'][0]['name'], pop)
                    bestpop = pop
                elif pop == bestpop:
                    mostpop = mostpop + " AND {} by {}. Popularity: {}.".format(t['name'], t['artists'][0]['name'], pop)

                id = t['id']
                trackinfo = sp.audio_features(id)

                d = trackinfo[0]['danceability']
                e = trackinfo[0]['energy']
                a = trackinfo[0]['acousticness']
                v = trackinfo[0]['valence']

                l_dance.append(d)
                l_en.append(e)
                l_aco.append(a)
                l_val.append(v)

                if d > best_dance:
                    most_danceable = "{} by {}. ({}) Danceability: {}.".format(t['name'], t['artists'][0]['name'], year, d)
                    best_dance = d
                elif d == best_dance:
                    most_danceable = most_danceable + " AND {} by {}. ({}) Danceability: {}.".format(t['name'], t['artists'][0]['name'], year, d)

                if e > best_en:
                    most_energetic = "{} by {}. ({}) Energy: {}.".format(t['name'], t['artists'][0]['name'], year, e)
                    best_en = e
                elif e == best_en:
                    most_energetic = most_energetic + " AND {} by {}. ({}) Energy: {}.".format(t['name'], t['artists'][0]['name'], year, e)

                if a > best_aco:
                    most_acoustic = "{} by {}. ({}) Acousticness: {}.".format(t['name'], t['artists'][0]['name'], year, a)
                    best_aco = a
                elif a == best_aco:
                    most_acoustic = most_acoustic + " AND {} by {}. ({}) Acousticness: {}.".format(t['name'], t['artists'][0]['name'], year, a)

                if v > best_val:
                    happiest = "{} by {}. ({}) Valence: {}.".format(t['name'], t['artists'][0]['name'], year, v)
                    best_val = v
                elif v == best_val:
                    happiest = happiest + " AND {} by {}. ({}) Valence: {}.".format(t['name'], t['artists'][0]['name'], year, v)


        #Calculate year averages and add to lists
        dance.append(calculate_average(l_dance))
        en.append(calculate_average(l_en))
        aco.append(calculate_average(l_aco))
        val.append(calculate_average(l_val))

        years.append(year)
        most_populars.append(mostpop)

    #Zip year and most popular song to a list of 2-valued tuples
    yearly_populars = zip(years, most_populars)

    context = {"years": years, "danceability": dance, "energy": en,
    "acousticness": aco, "valence": val, "yearly_populars": yearly_populars,
    "most_acoustic": most_acoustic, "most_energetic": most_energetic,
    "most_danceable": most_danceable, "happiest": happiest}

    return render(request, 'analysis.html', context)

