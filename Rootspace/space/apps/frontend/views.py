
from django.template.response import TemplateResponse
from django.http import HttpResponse


# Create your views here.
def index(request):
    html = TemplateResponse(request, 'index.html')
    return HttpResponse(html.render())


def all_messages(request):
    html = TemplateResponse(request, 'all_messages.html')
    return HttpResponse(html.render())


def dread_messages(request):
    html = TemplateResponse(request, 'dread_messages.html')
    return HttpResponse(html.render())


def read_messages(request):
    html = TemplateResponse(request, 'read_messages.html')
    return HttpResponse(html.render())
    
    


def create_token(request):
    html = TemplateResponse(request, 'create_token.html')
    return HttpResponse(html.render())
    
def active_token(request):
    html = TemplateResponse(request, 'active_token.html')
    return HttpResponse(html.render())
      

