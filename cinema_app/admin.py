from django.contrib import admin
from .models import Film, Seance

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ['titre', 'date_sortie', 'duree_minutes']

@admin.register(Seance)
class SeanceAdmin(admin.ModelAdmin):
    list_display = ['film', 'date_heure', 'salle', 'places_disponibles']