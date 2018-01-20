
from django.template.response import TemplateResponse
from django.http import HttpResponse


# Create your views here.
def index(request):


    html = TemplateResponse(request, 'index.html')
    return HttpResponse(html.render())

