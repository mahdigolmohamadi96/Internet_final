import hashlib
import logging

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from Internet.models import LoginDB
from game.models import Gamedb, GameComment, UserComment

logger = logging.getLogger('django')


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        model = LoginDB
        fields = ('username', 'password')

    # def validate(self, data):
    #     username = data.get('username')
    #     password = data.get('password')
    #     if username:
    #         if password:
    #             try:
    #                 LoginDB.objects.get(password=password, username=username)
    #             except Exception as e:
    #                 logger.log(logging.INFO, e.args)
    #                 raise ValidationError('incorrect username or password')
    #             return data
    #         else:
    #             raise ValidationError('password cannot be empty')
    #     else:
    #         raise ValidationError('username cannot be empty')


class signUpserializer(serializers.ModelSerializer):
    class Meta:
        model = LoginDB
        fields = ('username', 'password', 'first_name', 'last_name', 'email', 'sex', 'birth_date')

    def create(self, validated_data):
        return LoginDB.objects.create_user(**validated_data)


class GameRate(serializers.ModelSerializer):
    class Meta:
        model = Gamedb
        fields = ('gameName', 'gamerate')


class MaxPlayed(serializers.ModelSerializer):
    class Meta:
        model = Gamedb
        fields = ('gameName', 'playedTimes')


class NewGames(serializers.ModelSerializer):
    class Meta:
        model = Gamedb
        fields = ('gameName', 'date', 'gamerate')


class Comment(serializers.ModelSerializer):

    def validate_user(self, data):
        print(self.context['request'].user)
        return self.context['request'].user

    class Meta:
        model = GameComment
        fields = ('text', 'stars', 'game')


class CommentUser(serializers.ModelSerializer):

    # def validate_user(self, data):
    #     print(self.context['request'].user)
    #     return self.context['request'].user

    class Meta:
        model = UserComment
        fields = ('text', 'user', 'touser')
