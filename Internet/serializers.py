import hashlib
import logging

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from Internet.models import LoginDB

logger = logging.getLogger('django')


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        model = LoginDB
        fields = ('username','password')

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

class signUpserializer (serializers.ModelSerializer):
    class Meta:
        model = LoginDB
        fields = ('username','password' , 'first_name' , 'last_name' , 'email' , 'sex','birth_date')


    def create(self, validated_data):
        return LoginDB.objects.create_user(**validated_data)

