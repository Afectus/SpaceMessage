
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