"""Internet_final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import Internet
from Internet.views import login, Home, UserHome, Signout, ShowMaxRate, ShowMaxPlayed, ShowNewGames, RateGames, get_rate
from Internet.views import SignUp
from django.conf import settings


from django.conf.urls.static import static

from game.views import MakeGame, GamePlay, GameKind

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login.as_view()),
    path('signup/',SignUp.as_view()),
    path('signout/',Signout.as_view()),
    path('home/',Home.as_view()),
    path('userHome/',UserHome.as_view()),
    path('makeGame/',MakeGame.as_view()),
    path('playGame/',GamePlay.as_view()),
    path('gamekinds/',GameKind.as_view()),
    path('bestGames/',ShowMaxRate.as_view()),
    path('mostGamesPlayed/',ShowMaxPlayed.as_view()),
    path('newGames/',ShowNewGames.as_view()),
    path('rateGame/', get_rate ),
    path('rated/',RateGames.as_view(), name='rateGame' )
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




