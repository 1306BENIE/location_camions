from django.db import models

class Camion(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    annee = models.IntegerField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.marque} {self.modele} ({self.annee})"

class Client(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Location(models.Model):
    camion = models.ForeignKey(Camion, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_debut = models.DateField()
    date_fin = models.DateField()

    def __str__(self):
        return f"{self.camion} - {self.client}"
    
    
    





