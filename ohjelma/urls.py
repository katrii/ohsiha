from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name = 'home'),
    path('songs/', views.SongList.as_view(), name = 'song_list'),
    path('view/<int:pk>', views.SongView.as_view(), name = 'song_view'),
    path('new', views.SongCreate.as_view(), name = 'song_new'),
    path('view/<int:pk>', views.SongView.as_view(), name = 'song_view'),
    path('edit/<int:pk>', views.SongUpdate.as_view(), name = 'song_edit'),
    path('delete/<int:pk>', views.SongDelete.as_view(), name = 'song_delete'),
    path('tracks/', views.TrackView, name = 'track_list'),
    path('yearanalysis/', views.YearAnalysis, name = 'year_analysis'),
    path('analysis/<int:pk>', views.Analysis.as_view(), name = 'track_detail'),

    #url(r'^tracks/(?P<tracksyear>\w+)/$', views.TrackView, name = "TrackView")
    path('tracks/<int:tracksyear>', views.TrackView, name = "TrackView")
]
