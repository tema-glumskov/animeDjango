"""
URL configuration for sites project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from animesite.views import index, anime, manga, register

urlpatterns = [
    path('admin/', admin.site.urls),
    # обслуживание корня сайта
    path('', index, name='index'),
    # обслуживание страницы аниме
    path('anime/', anime, name='anime'),
    # обслуживание страницы манги
    path('manga/', manga, name='manga'),
    # обслуживание страницы регистрации
    path('register/', register, name='register'),  # заменить на реальную регистрацию страницу
]
