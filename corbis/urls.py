from django.conf.urls import patterns, url
from django.conf import settings
from app.views import Home
from django.conf.urls.static import static


urlpatterns = patterns('',
                       url(r'^$', Home.as_view(), name='Home'),
                       ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

