from datetime import date
from django.shortcuts import render
from .models import Film

def accueilView(request):
    films = Film.objects.all()[:3]
    return render(request, "accueil.html", {"today": date.today(), "films": films})

def filmsView(request):
    films = Film.objects.all()
    return render(request, "films.html", {"today": date.today(), "films": films})

def aproposView(request):
    return render(request, "apropos.html", {"today": date.today()})