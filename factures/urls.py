from django.urls import path
from . import views

urlpatterns = [
    path('creer/', views.creer_facture, name='creer_facture'),
    path('cree/', views.facture_cree, name='facture_cree'),
    path('modifier/<int:facture_id>/', views.modifier_facture, name='modifier_facture'),
    path('liste/', views.liste_factures, name='liste_factures'),
    path('supprimer/<int:facture_id>/', views.supprimer_facture, name='supprimer_facture'),
    path('details/<int:facture_id>/', views.details_facture, name='details_facture'),

]

