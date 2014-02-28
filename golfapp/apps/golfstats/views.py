from django.shortcuts import render
from golfapp.apps.golfstats.models import Golfer
from golfapp.apps.golfstats.forms import GolferForm

#def index(request):
#    return render(request, 'golfstats/index.html', {})

def modifyGolfers(request):
    players = Golfer.objects.all()
    return render(request, 'golfstats/modify-golfer.html', {'players': players})

def listGolfers(request):
    players = Golfer.objects.all()
    return render(request, 'golfstats/list.html', {'players': players})

#def getGolferForm(request


def modifyGolferForm(request):
    if request.method == "POST":
        form = GolferForm(request.POST)
        if form.is_valid():
            model_instance = form.save()
            return redirect('victory')
    else:
        form = GolferForm()

    return render(request, "golfstats/modify-golfer-form.html", {'form': form})
