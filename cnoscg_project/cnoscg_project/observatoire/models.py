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
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    prefecture = models.ForeignKey(Prefecture, on_delete=models.CASCADE)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)
    picture = models.FileField(upload_to="images", blank=True)

    def _str_(self):
        return f"{self.nom}{self.prenom}"