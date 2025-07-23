from django.db import models
import datetime

class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Client(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    telephone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nom
    
class Facture(models.Model):
    titre = models.CharField(max_length=200)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=datetime.date.today)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    payee = models.BooleanField(default=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titre} - {self.client.nom} - {self.montant} €"


categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, blank=True)

