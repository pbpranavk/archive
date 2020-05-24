"""exploreDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include, path
from django.views.generic.base import TemplateView 
from .views import home
urlpatterns = [
    path('login/', include(('login.urls','login'), namespace="login")),
    path('problem/', include(('ask.urls','ask'),namespace='ask')),
    path('admin/', admin.site.urls),
    path('loginTest/', include('django.contrib.auth.urls')),
    path('', home, name='home'),
    path('questions/',include(('questions.urls','questions'), namespace='questions')),
]
