import copy

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from Internet.models import LoginDB
from Internet.permissions import CheckAuth, Auth
from Internet.serializers import signUpserializer, LoginSerializer, GameRate, MaxPlayed, NewGames, Comment, CommentUser
from Internet_final.settings import online, which
from game.models import Gamedb, GameComment, UserComment


class login(APIView):
    permission_classes = ()

    def get(self, req):
        return render(req, "index.html")

    def post(self, req):
        serializer = LoginSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(req, username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=User.objects.get(username=username))
            res = HttpResponseRedirect(redirect_to='/home')
            res.set_cookie('tk', token.key, 12344312, 8700)
            return res
        else:
            return Response({'message': 'login failed!'}, status=status.HTTP_401_UNAUTHORIZED)


class SignUp(APIView):
    permission_classes = ()

    def get(self, req):
        return render(req, "signUp.html")

    def post(self, req):
        s = signUpserializer(data=req.data)
        s.is_valid(True)

        return HttpResponseRedirect(redirect_to='profile.html')


class Home(APIView):
    permission_classes = (CheckAuth,)

    def get(self, req):
        # print('req == ', req.user)
        a = LoginDB.objects.get(username=req.user)
        # print(Gamedb.objects.values('gamerate', 'gameName').order_by('-gamerate')[0])
        return render(req, "user.html", {'Username': a.username, 'bestGame':

            Gamedb.objects.values('gamerate', 'gameName').order_by('-gamerate')[0]['gameName'], 'mostOnline': 0,
                                         'bestNew':
                                             Gamedb.objects.values('date', 'gameName', 'gamerate').order_by('-date',
                                                                                                            'gamerate')[
                                                 0]['gameName'],
                                         'onlines': [x.username for x in online], 'mail': a.email, 'name': a.first_name,
                                         'lstname': a.last_name})


class UserHome(APIView):
    permission_classes = (CheckAuth,)

    def get(self, req):
        return Response("loged in succesfully!")


class Signout(APIView):
    def get(self, req):
        try:
            Token.objects.get(user=req.user).delete()
            online.remove(req.user)
            return render(req, "logedOut.html")
        except:
            return Response("not loged out")


# API
class ShowMaxRate(ListAPIView):
    serializer_class = GameRate

    def get_queryset(self):
        return Gamedb.objects.values('gamerate', 'gameName').order_by('-gamerate')


# API
class ShowMaxPlayed(ListAPIView):
    serializer_class = MaxPlayed

    def get_queryset(self):
        return Gamedb.objects.values('playedTimes', 'gameName').order_by('-playedTimes')


# API
class ShowNewGames(ListAPIView):
    serializer_class = NewGames

    def get_queryset(self):
        return Gamedb.objects.values('date', 'gameName', 'gamerate').order_by('-date', 'gamerate')


@api_view(['GET'])
def get_rate(req):
    return render(req, "ratingGame.html")


class RateGames(APIView):
    authentication_classes = (Auth,)

    # serializer_class = Comment
    # queryset = GameComment.objects.all()

    def post(self, req):
        a = Comment(data=req.data)
        a.is_valid(True)
        com = GameComment(**a.validated_data)
        com.user = req.user
        com.save()
        b = CommentUser(data=req.data)
        b.is_valid(True)
        com2 = UserComment(**b.validated_data)
        com2.user = b.validated_data['user']
        com2.touser = b.validated_data['touser']
        com2.save()

        return Response('mmammmad nooobari')
