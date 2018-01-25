
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.

class SpaceViewSetTrue(viewsets.ModelViewSet):
    queryset = SpaceMessage.objects.all().filter(status=True)
    serializer_class = SpaceMessageSerializer

class SpaceViewSet1False(viewsets.ModelViewSet):
    queryset = SpaceMessage.objects.all().filter(status=False)
    serializer_class = SpaceMessageSerializer

class SpaceViewSet1All(viewsets.ModelViewSet):
    queryset = SpaceMessage.objects.all()
    serializer_class = SpaceMessageSerializer




    
class TokenGeneratorSet1All(viewsets.ModelViewSet):
    queryset = TokenGenerator.objects.all()
    serializer_class = TokenGeneratorSerializer
