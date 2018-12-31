from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

from Internet.serializers import signUpserializer


class login(APIView):
    def get(self,req):
        return render(req , "index.html")

    # def post(self,req):

class SignUp(APIView):
    def get(self,req):
        return render(req, "signUp.html")
    def post(self,req):
        s = signUpserializer(data=req.data)
        s.is_valid(True)
        s.save()
        return HttpResponseRedirect(redirect_to='profile.html')
