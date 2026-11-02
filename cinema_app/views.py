from datetime import date
from django.shortcuts import render

def accueilView(request):
    return render(request, "accueil.html", {"today": date.today()})

def aproposView(request):
    return render(request, "apropos.html", {"today": date.today()})