
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include('space.apps.backend.urls')),
    url(r'', include('space.apps.frontend.urls')),
]
