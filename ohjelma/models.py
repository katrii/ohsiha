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
        