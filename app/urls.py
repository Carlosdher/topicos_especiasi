from __future__ import unicode_literals

from django.urls import include, path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from . import views as anime

app_name = 'app'

urlpatterns = [


    path('', anime.Home.as_view(), name='inicial'),

    #forum
    path('forum', anime.Forum.as_view(), name='forum'),

    path('forum/<pk>', anime.AdicionarRespotas.as_view(), name='participar'),

    path('arts', anime.TimeLine.as_view(), name='arts'),
    path('animes', anime.Animes.as_view(), name='anime'),
    path('criar-arte', anime.CriarArte.as_view(), name='criar_arte'),
    path('criar-forum', anime.CriarForum.as_view(), name='criar_forum'),

    ]
