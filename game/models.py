import random
import string

from django.db import models

# Create your models here.
from Internet.models import LoginDB


class Gamedb(models.Model):
    gameName= models.CharField(max_length=30 , default='')
    gamerate = models.IntegerField(default=0) #game rates(points)
    date = models.DateTimeField(auto_now=True)
    max = models.IntegerField(default=100)
    hold = models.CharField(max_length=10)
    dice = models.IntegerField(default=1)
    dicetimes = models.IntegerField(default=10)
    user = models.ForeignKey(LoginDB , on_delete=models.CASCADE)
    timesplayed = models.IntegerField(default=0)
    avgpoint = models.IntegerField(default=0) #avrage of game rate
    playedTimes = models.IntegerField(default=0)# how many times played
    playedUsers = models.IntegerField(default=0)# how many people played





class GameData:
    def __init__(self, dice_count, max_score, hold):
        self.id = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=32))
        self.dices = []
        self.dice_count = dice_count
        self.turn = 0
        self.max_score = max_score
        self.player1_current = 0
        self.player1_total = 0
        self.player2_current = 0
        self.player2_total = 0
        self.winner = None
        self.hold = hold
        self.mid = None