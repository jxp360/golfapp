from django.shortcuts import render
from golfapp.apps.golfstats.models import Golfer

def index(request):
    return render(request, 'golfstats/index.html', {})

def golfers(request):
    players = Golfer.objects.all()
    return render(request, 'golfstats/golfers.html', {'players': players})
