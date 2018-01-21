
from rest_framework import viewsets
from .models import SpaceMessage
from .serializers import SpaceMessageSerializer

# Create your views here.

class SpaceViewSetTrue(viewsets.ModelViewSet):
    queryset = SpaceMessage.objects.all().filter(status=True)
    serializer_class = SpaceMessageSerializer

class SpaceViewSet1False(viewsets.ModelViewSet):
    queryset = SpaceMessage.objects.all().filter(status=False)
    serializer_class = SpaceMessageSerializer

def index(request):
    html = TemplateResponse(request, 'index.html')
    return HttpResponse(html.render())

class SpaceViewSet1All(viewsets.ModelViewSet):
    queryset = SpaceMessage.objects.all()
    serializer_class = SpaceMessageSerializer
