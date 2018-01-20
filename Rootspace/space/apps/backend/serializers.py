from rest_framework import serializers
from .models import *


class SpaceMessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SpaceMessage
        fields = ('id', 'title', 'text', 'date',  'status')