from django.urls import path,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

#ici on importe les fonctions créeer dans vues
from . import views


urlpatterns = [
    path('', views.realisation, name="realisation")
]

