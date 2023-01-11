from django.shortcuts import render,redirect
from .models import *
from .forms import RentForm,ClientForm
#from django.contrib.auth import authenticate
from django.http import HttpResponse

def locations(request):
    location = Location.objects.all()
   
    return render(request,'mini_projets/base.html',{'locations':location})

def clientele(request,id):
    client = Client.objects.get(pk=id)
   
    return render(request,'mini_projets/info_client.html',{'clients':client})

def voitures(request,id):
    car = Vehicule.objects.get(pk=id)
    type_vehicule = car.type
    taille_vehicule = car.taille
    
   
    return render(request,'mini_projets/info_vehicule.html',{'cars':car,'type_vehicule':type_vehicule,'taille_vehicule':taille_vehicule})

def les_vehicules(request):
    vehicule = Vehicule.objects.all()
    # type_vehicule = vehicule.type
    # taille_vehicule = vehicule.taille
   
    return render(request,'mini_projets/info_vehicule.html',{'vehicules':vehicule})


def premier(request):

    return render(request,'mini_projets/liste_locations.html')

def touteclientele(request):
    toute = Client.objects.all()
   
    return render(request,'mini_projets/info_client.html',{'toutes':toute})

def Form_page(request):
    if request.method == 'POST':
        form = RentForm(request.POST)
        if form.is_valid():
            # les données du formulaire sont valides, vous pouvez les enregistrer en base de données ou les traiter de quelque autre manière
            #
            form.save()
            return redirect('rent')
            
        else:
            return render(request,'mini_projets/addlocation.html',context={'form':form})
    else:
        form = RentForm()
        return render(request,'mini_projets/addlocation.html',context={'form':form})
    #return HttpResponse(context={'form':formulaire})

def Client_page(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            # les données du formulaire sont valides, vous pouvez les enregistrer en base de données ou les traiter de quelque autre manière
            #
            form.save()
            return redirect('rent')
            
        else:
            return render(request,'mini_projets/addclient.html',context={'form':form})
    else:
        form = ClientForm()
        return render(request,'mini_projets/addclient.html',context={'form':form})
    #return HttpResponse(context={'form':formulaire})


# Create your views here.

