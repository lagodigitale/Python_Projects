from django import forms
from .models import Client,Location

class RentForm(forms.ModelForm):
    class Meta:
        model=Location
        fields= '__all__'

class ClientForm(forms.ModelForm):
    class Meta:
        model=Client
        fields= '__all__'
   
    # def save(self):
    #     # récupère les données du formulaire et enregistre les objets de modèle appropriés en base de données
    #     client = self.cleaned_data['client']
    #     vehicule = self.cleaned_data['vehicule']
    #     location = Location.objects.create(location)


# class ClientForm(forms.Form):
#     username=forms.CharField(max_length=80, label='Nom dutilisateur')
#     userprename=forms.CharField(max_length=80, label='Nom dutilisateur')
#     mail=forms.CharField(max_length=80, label='Mail')
#     num =forms.IntegerField(max_length=80, label='Numero')
#     adresse =forms.IntegerField(max_length=80, label='Adresse')
#     ville=forms.CharField(max_length=80, label='ville')
#     pays=forms.CharField(max_length=80, label='pays')









   