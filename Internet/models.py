from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class LoginDB(User):
    # username = models.CharField(max_length=100)
    # first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)
    photo = models.FileField()
    games_count = models.IntegerField(null=True)
    # email = models.EmailField()
    average_game_score = models.FloatField(null=True)
    average_user_score = models.FloatField(null=True)
    birth_date = models.DateField()
    sex = models.CharField(max_length=7)
    # password = models.CharField(max_length=30)
