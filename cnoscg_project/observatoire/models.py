from django.db import models

class Observateur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20, unique=True)
    region = models.CharField(max_length=100)
    prefecture = models.CharField(max_length=150)
    commune = models.CharField(max_length=150)
    picture = models.FileField(upload_to="images", blank=True)
    #statut = models.CharField(max_length=50, default="Actif")

    def _str_(self):
        return f"{self.nom}{self.prenom}"