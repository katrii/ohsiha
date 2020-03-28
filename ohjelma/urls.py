from django.urls import path
from . import views

urlpatterns = [
    #path('index/', views.index, name='index'),
    #path('login/', views.login_form, name ='login'),
    #path('logout/', views.logout_form, name ='logout'),
    #path('signup/', views.signup, name ='signup'),
    #path('home/', views.home, name ='home'),
    path('', views.SongList.as_view(), name = 'song_list'),
    path('view/<int:pk>', views.SongView.as_view(), name = 'song_view'),
    path('new', views.SongCreate.as_view(), name = 'song_new'),
    path('view/<int:pk>', views.SongView.as_view(), name = 'song_view'),
    path('edit/<int:pk>', views.SongUpdate.as_view(), name = 'song_edit'),
    path('delete/<int:pk>', views.SongDelete.as_view(), name = 'song_delete'),
]
