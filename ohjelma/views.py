#from django.shortcuts import render
from django.http import HttpResponse

#def index(request):
#    return HttpResponse("Hey there world!")

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from ohjelma.models import Song

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