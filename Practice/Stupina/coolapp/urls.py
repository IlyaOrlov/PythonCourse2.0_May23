from django.urls import path
from . import views

# ---если сюда приходит код какой-то,мы при помощи шаблона urlpatterns перенаправляем этот код в views.index.
# name='index' - это псевдоним для получившегося url, чтоб удобней было обращаться к тому же ресурсу (функции)
# из кода в некоторых случаях.

urlpatterns = [
    path('', views.index, name='index'),
    path('films/', views.films, name='films'),
    path('new/', views.new, name='new'),
    # если в запросе число:
    path('<int:film_id>/', views.new, name='new'),
]
