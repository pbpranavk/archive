"""quora_clone URL Configuration

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
from signup.views.home import HomeView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('change-password', auth_views.PasswordChangeView.as_view(template_name='change-password.html'), name = "change-password"),
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('signup/',include(('signup.urls',"signup"), namespace = "signup")),
    path('questions/',include(('questions.urls','questions'),namespace= 'questions')),
    path('home',HomeView.home,name="home" ),

]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
