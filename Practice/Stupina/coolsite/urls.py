"""
URL configuration for coolsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls import include
from django.urls import path
from django.contrib import admin

# --прописываем связь с coolapp.urls
# Когда мы обращаемся к серверу (127.0.0.1:8000) приходит запрос,
# сервер начинает анализировать, что дальше идет посде запроса : # к какому ресурсу/файлу/скрипту на сервере идет обращение.
# 127.0.0.1:8000 - пустой запрос
# Если запрос 127.0.0.1:8000/coolapp/ - попадая в главный файл URL, указанная часть URL (coolapp)
# будет сравниваться с каждым шаблоном из списка (coolapp/ - шаблон). Если шаблон совпал, анализируется дальше.
# include('coolapp.urls') - расширяет шаблон:  path('coolapp/', views.index, name='index'),
# и вызывается coolapp.views.index---


urlpatterns = [
    path('admin/', admin.site.urls),
    path('coolapp/', include('coolapp.urls')),
    path('', include('coolapp.urls')),
]
