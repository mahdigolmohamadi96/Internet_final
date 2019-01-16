import json
import random

from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from Internet.permissions import CheckAuth, Auth
from Internet_final.settings import games, gamesPlay
from game import serializer
from game.models import Gamedb, GameData
from game.serializer import MakeGameSerializer


class MakeGame(APIView):
    permission_classes = (CheckAuth,)
    authentication_classes = (Auth,)

    def get(self, req):
        return render(req, "MakeGame.html")

    def post(self, req):
        s = MakeGameSerializer(data=req.data)
        s.is_valid(True)
        g = Gamedb(**s.validated_data)
        g.user = req.user
        g.save()
        print(req.data)
        return HttpResponseRedirect(redirect_to='profile.html')


class GamePlay(APIView):
    # permission_classes = (IsAuthenticated,)
    authentication_classes = (Auth,)

    @staticmethod
    def get(req):
        game_id = req.query_params.get('id')
        if game_id:
            game = Gamedb.objects.get(id=game_id)
            if (len(gamesPlay) == 0):
                new_game = GameData(game.dice, game.max, [int(x) for x in game.hold.split(',')])
                games[new_game.id] = new_game
                gamesPlay.add(new_game)
            else : new_game = gamesPlay.pop()

            return render(req, "internet.html",
                          {'winlimit': game.max, 'holdnum': game.hold, 'maxdice': game.dicetimes, 'dicenum': game.dice,
                           'gameid': new_game.id, 'dice': [1, 2], 'turn': 0, 'p1_current': 0, 'p1_total': 0,
                           'p2_current': 0, 'p2_total':0 , 'winner': 2 })
        raise NotFound('Game not found!')

    @staticmethod
    def post(request):
        action = request.data.get('action')
        game_id = request.data.get('game_id')
        if not game_id:
            raise ValidationError('game_id not found')
        if not action:
            raise ValidationError('action not found')
        game: GameData = games.get(game_id)
        if not game:
            raise NotFound('game not found')
        game.mid = request.user.id
        if action == 'roll-dice':
            randoms = []
            change_turn = False
            for i in range(game.dice_count):
                rand = random.randrange(1, 7)
                change_turn = change_turn or (rand in game.hold)
                randoms.append(rand)
            if change_turn:
                # game.turn = not game.turn


                print(request.user.id)
                if game.turn == request.user.id:
                    game.turn =0
                elif game.turn == 0:
                    game.turn = request.user.id
                print(game.turn)

                game.player1_current = 0
                game.player2_current = 0
            game.dices = randoms
            if game.turn:
                game.player1_current += sum(randoms)
            else:
                game.player2_current += sum(randoms)
        elif action == 'hold':
            game.player1_total += game.player1_current
            game.player1_current = 0
            game.player2_total += game.player2_current
            game.player2_current = 0
            # game.turn = not game.turn


            if game.turn == request.user.id:
                game.turn = 0
            elif game.turn == 0:
                game.turn = request.user.id
            print(game.turn)


            if game.player1_total >= game.max_score:
                game.winner = True
            if game.player2_total >= game.max_score:
                game.winner = False
        # print(game.__dict__)
        return Response(json.dumps(game.__dict__))


class GameKind(APIView):
    permission_classes = (CheckAuth,)
    authentication_classes = (Auth,)

    def get(self, req):
        a = Gamedb.objects.all()
        return render(req, "gameSelect.html", {'games': a})


