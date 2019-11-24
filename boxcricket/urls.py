from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('games/<id>', views.detail_game, name='detail_game'),
    path('games/', views.list_games, name='list_games'),
    path('games/new/', views.new_game, name='new_game'),
]
