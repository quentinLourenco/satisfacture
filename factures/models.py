from django.db import models
import datetime

class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Facture(models.Model):
    titre = models.CharField(max_length=200)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=datetime.date.today)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titre} - {self.montant} €"
