import logging

from django.core.exceptions import ValidationError
from rest_framework import serializers

from game.models import Gamedb

logger = logging.getLogger('django')


class MakeGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gamedb
        fields = ('gameName','hold', 'max', 'dice', 'dicetimes')

    def validate_hold(self, data):
        print(data)

        holds = data.split(',')
        try:
            for i in holds:
                b = int(i)
                if 6 >= b >= 1:
                    continue
                else:
                    raise ValidationError('hold nimbers out of Range')
        except ValueError:
            raise ValidationError('ridiiii')

        return data
