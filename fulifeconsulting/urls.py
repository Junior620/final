"""fulifeconsulting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from .views import index, contact

urlpatterns = [
    path('', index, name="index"),
    path('acceuil/',include('acceuil.urls')),
    path('contact/',include('contact.urls')),
    path('propos/',include('apropos.urls')),
    path('realisation/', include('realisation.urls')),
    path('services/', include('services.urls')),
    #path('contact', contact, name="contact"),
    path('admin/', admin.site.urls),
    path('', include('chatbot.urls')),
]


#handler404= 'acceuil.views.error_404'




