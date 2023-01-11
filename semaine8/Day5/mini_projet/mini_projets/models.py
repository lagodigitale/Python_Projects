from django.db import models
from django.contrib.auth.models import AbstractUser


class Client(models.Model):
    nom = models.CharField(max_length=200, null=True)
    prenom = models.CharField(max_length=200,null=True)
    messagerie_electronique = models.CharField(max_length=200,null=True)
    num = models.IntegerField()
    adresse = models.IntegerField()
    ville = models.CharField(max_length=200, null=True)
    pays = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.nom






class TypeVehicule(models.Model):
    nom = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.nom

class TailleVehicule(models.Model):
    nom = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.nom


class Vehicule(models.Model):
    type = models.ForeignKey(TypeVehicule, on_delete=models.CASCADE)
    created_date = models.CharField(max_length=200,null=True)
    cout = models.IntegerField()
    taille =  models.ForeignKey(TailleVehicule, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.cout)


class Location(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    location_date = models.CharField(max_length=200,null=True)    
    return_date = models.CharField(max_length=200,null=True)
    def __str__(self):
        return str(self.location_date)
    

class TarifLocation(models.Model):
    taille_vehicule = models.ForeignKey(TailleVehicule, on_delete=models.CASCADE)
    type_vehicule = models.ForeignKey(TypeVehicule, on_delete=models.CASCADE)
    tarif = models.CharField(max_length=200,null=True) 
    def __str__(self):
        return str(self.tarif)   



# class User(AbstractUser):
#     ADMIN= 'ADMIN'
#     CUSTOMER ='CUSTOMER'

#     ROLE = [(ADMIN,'Admin'),(CUSTOMER, 'CUSTOMER'),]
#     profile_photo = models.ImageField(verbose_name='Photo de profil')
#     role = models.CharField(max_length=30,choices=ROLE,verbose_name='Role')


# Create your models here.

    

