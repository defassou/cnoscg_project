from django.db import models


class Region(models.Model):
    nom = models.CharField(max_length=100)

    def _str_(self):
        return f"{self.nom}"


class Prefecture(models.Model):
    nom = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def _str_(self):
        return f"{self.nom}"


class Commune(models.Model):
    nom = models.CharField(max_length=100)
    prefecture = models.ForeignKey(Prefecture, on_delete=models.CASCADE)

    def _str_(self):
        return f"{self.nom}"


class Observateur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20, unique=True)
    region = models.CharField(max_length=100)
    prefecture = models.CharField(max_length=150)
    commune = models.CharField(max_length=150)
    picture = models.FileField(upload_to="images", blank=True)

    # statut = models.CharField(max_length=50, default="Actif")

    def _str_(self):
        return f"{self.prenom}{self.nom}"
