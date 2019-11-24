from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('games/<int:id>', views.game_details, name='game_details'),
    path('games/', views.games, name='games'),
    path('games/new/', views.new_game, name='new_game'),
]
