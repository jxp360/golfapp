from django.shortcuts import render, redirect
from golfapp.apps.golfstats.models import Golfer, GolfCourse
from golfapp.apps.golfstats.forms import GolferForm, GolfCourseForm
from django.forms.models import modelformset_factory

#def index(request):
#    return render(request, 'golfstats/index.html', {})

#def modifyGolferFormset(request):
#    GolferFormSet = modelformset_factory(Golfer)
#    if request.method == "POST":
#        formset = GolferFormSet(request.POST, request.FILES)
#        if formset.is_valid():
#            formset.save()
#    else:
#        formset = GolferFormSet()
#    return render(request, "golfstats/modify-golfer-formset.html", {'formset': formset})

def listGolfers(request):
    players = Golfer.objects.all()
    return render(request, 'golfstats/list-golfers.html', {'players': players})

def addGolferForm(request):
    if request.method == "POST":
        form = GolferForm(request.POST)
        if form.is_valid():
            model_instance = form.save()
            return redirect('golfstats.list-golfers')
    else:
        form = GolferForm()
    return render(request, 'golfstats/add-golfer.html', {'form': form})

def modifyGolferForm(request, golfer_id):
    golfer = Golfer.objects.get(pk=golfer_id)
    if request.method == "POST":
        form = GolferForm(request.POST, instance=golfer)
        if form.is_valid():
            model_instance = form.save()
            return redirect('golfstats.list-golfers')
    else:
        form = GolferForm(instance=golfer)
    return render(request, 'golfstats/modify-golfer.html', {'golfer_id': golfer_id, 'form': form})

def listCourses(request):
    courses = GolfCourse.objects.all()
    return render(request, 'golfstats/list-courses.html', {'courses': courses})

def addCourseForm(request):
    if request.method == "POST":
        form = GolfCourseForm(request.POST)
        if form.is_valid():
            model_instance = form.save()
            return redirect('golfstats.list-courses')
    else:
        form = GolfCourseForm()
    return render(request, 'golfstats/add-course.html', {'form': form})

def modifyCourseForm(request, course_id):
    course = GolfCourse.objects.get(pk=golfer_id)
    if request.method == "POST":
        form = GolfCourseForm(request.POST, instance=course)
        if form.is_valid():
            model_instance = form.save()
            return redirect('golfstats.list-courses')
    else:
        form = GolfCourseForm(instance=course)
    return render(request, 'golfstats/modify-course.html', {'course_id': golfer_id, 'form': form})

