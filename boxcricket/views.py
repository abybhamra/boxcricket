from django.shortcuts import render, redirect

from boxcricket.forms import GameForm
from boxcricket.models import Game


def home(request):
    return render(request, "boxcricket/home.html", {'name': 'Abhineet'})


def list_games(request):
    return render(request, "boxcricket/games.html", {'games': Game.objects.all()})


def new_game(request):
    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.save()
            return redirect('list_games')
    else:
        form = GameForm()
    return render(request, 'boxcricket/new_game.html', {'form': form})


def detail_game():
    return None
