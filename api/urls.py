from django.contrib import admin
from django.urls import path

from .api import api
from .constants import NinjaApi

urlpatterns = [
    path('admin/', admin.site.urls),
    path(NinjaApi.BASE_URL+NinjaApi.VERSION, api.urls),
]
