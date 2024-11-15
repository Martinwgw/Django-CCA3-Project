from django.shortcuts import render, redirect, get_object_or_404
from .models import Game
from .forms import GameForm

#create
def game_create(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('game_list')
    else:
        form = GameForm()
    return render(request, 'game_form.html', {'form':form})

#read
def game_list(request):
    games = Game.objects.all()
    return render(request, 'game_list.html', {'games':games})

#update game details
def game_update(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if request.method == 'POST':
        form = GameForm(request.POST,instance=game)
        if form.is_valid():
            form.save()
            return redirect('game_list')
    else:
        form = GameForm(instance=game)
    return render(request, 'game_form.html', {'form':form})

#delete game
def game_delete(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if request.method == 'POST':
        game.delete()
        return redirect('game_list')
    return render(request, 'game_delete.html', {'game': game})