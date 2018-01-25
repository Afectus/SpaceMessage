from rest_framework import serializers
from .models import *


class SpaceMessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SpaceMessage
        fields = ('id', 'title', 'text', 'date',  'status')
        
class TokenGeneratorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TokenGenerator
        fields = ('id', 'tokens')
