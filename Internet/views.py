from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from Internet.models import LoginDB
from Internet.permissions import CheckAuth
from Internet.serializers import signUpserializer, LoginSerializer, GameRate
from Internet_final.settings import online
from game.models import Gamedb


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
        print('req == ', req.user)
        a = LoginDB.objects.get(username=req.user)
        return render(req, "user.html", {'Username': a.username, 'onlines': [x.username for x in online], 'mail':a.email , 'name':a.first_name , 'lstname':a.last_name})


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


class ShowMaxRate(ListAPIView):
    serializer_class = GameRate
    def get_queryset(self):
        return Gamedb.objects.values('gamerate' , 'gameName').order_by('-gamerate')
