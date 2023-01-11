from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.premier,name='un'),
    path('rent',views.locations,name="rent"),
    path('info_client<int:id>/',views.clientele,name="info_client"),
    path('touteclientele',views.touteclientele,name="touteclientele"),
    path('cars<int:id>/',views.voitures,name="cars"),
    # path('info_vehicule/<int:id>/',views.voitures,name="info_vehicule"),
    path('vehicules',views.les_vehicules,name="vehicules"),

    path('add_location',views.Form_page,name='add'),
    path('add_client',views.Client_page,name='addc'),
    


    # path('/rent/rental/add',views,name='rent'),
    # path('/rent/customer/<pk>',views,name='rent'),
    # path('/rent/customer/',views,name='rent'),
    # path('/rent/customer/add',views,name='rent'),
    # path('/rent/vehicle/',views,name='rent'),
    # path('/rent/vehicle/<pk>',views,name='rent'),
    # path('/rent/vehicle/add',views,name='rent'),
   


]
