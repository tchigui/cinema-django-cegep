from django.db import models

class Film(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    duree_minutes = models.IntegerField()
    date_sortie = models.DateField()
    affiche = models.ImageField(upload_to='affiches/', blank=True, null=True)
    
    def __str__(self):
        return self.titre

class Seance(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='seances')
    date_heure = models.DateTimeField()
    salle = models.CharField(max_length=50)
    places_disponibles = models.IntegerField(default=80)
    
    def __str__(self):
        return f"{self.film.titre} — {self.date_heure.strftime('%d/%m/%Y %H:%M')}"