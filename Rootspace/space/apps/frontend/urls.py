"""space URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from .views import *
from rest_framework import routers


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'getmessall', all_messages, name='all_messages'),
    url(r'getdread_messages', dread_messages, name='dread_messages'),
    url(r'getread_messages', read_messages, name='read_messages'),
    url(r'create_token', create_token, name='create_token'),
    url(r'active_token', active_token, name='active_token'),

]

