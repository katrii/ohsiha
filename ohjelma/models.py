from django.db import models
from django.urls import reverse

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Song(models.Model):
    song_name = models.CharField(max_length=200)
    song_artist = models.CharField(max_length = 200)
    release_year = models.IntegerField(default=2000)

    def __str__(self):
        return self.song_name

    def get_absolute_url(self):
        return reverse('song_edit', kwargs={'pk': self.pk})

class Track(models.Model):
    track_id = models.CharField(max_length=30)     
    track_name = models.CharField(max_length=500)
    track_artist = models.CharField(max_length = 500)
    track_duration = models.CharField(max_length = 10)
    track_popularity = models.IntegerField(default=100)

    track_danceability = models.FloatField(max_length=10)
    track_energy = models.FloatField(max_length=10)
    track_key = models.IntegerField(max_length=3)
    track_loudness = models.FloatField(max_length=10)
    track_speechiness = models.FloatField(max_length=10)
    track_acousticness = models.FloatField(max_length=10)
    track_instrumentalness = models.FloatField(max_length=10)
    track_liveness = models.FloatField(max_length=10)
    track_valence = models.FloatField(max_length=10)
    track_tempo = models.FloatField(max_length=10)

    def __str__(self):
        return self.track_name


