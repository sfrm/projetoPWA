from django.conf.urls import url
from django.contrib import admin

from core.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^contato$',contato, name='contato' ),
    url(r'^produto$', produto , name='produto'),
    url(r'^produtos$', produtos, name='produtos'),
]
