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


routerFalse = routers.DefaultRouter()
routerFalse.register(r'get_messages/false', SpaceViewSet1False)

routerTrue = routers.DefaultRouter()
routerTrue.register(r'get_messages/true', SpaceViewSetTrue)

routerAll = routers.DefaultRouter()
routerAll.register(r'get_messages/all', SpaceViewSet1All)

routerTokenAll = routers.DefaultRouter()
routerTokenAll.register(r'get_token/all', TokenGeneratorSet1All)

routerTokenFalse = routers.DefaultRouter()
routerTokenFalse.register(r'get_token/false', TokenGeneratorSet1False)

routerTokenTrue = routers.DefaultRouter()
routerTokenTrue.register(r'get_token/true', TokenGeneratorSet1True)

urlpatterns = [

    url(r'', include(routerFalse.urls)),
    url(r'', include(routerTrue.urls)),
    url(r'', include(routerAll.urls)),
    url(r'', include(routerTokenAll.urls)),
    url(r'', include(routerTokenFalse.urls)),
    url(r'', include(routerTokenTrue.urls)),

]


