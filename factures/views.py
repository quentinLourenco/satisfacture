from django.shortcuts import render, redirect, get_object_or_404
from .forms import FactureForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Facture, Categorie, Client


def creer_facture(request):
    if request.method == 'POST':
        form = FactureForm(request.POST)
        if form.is_valid():
            facture = form.save(commit=False)

            if not facture.categorie:
                autres, _ = Categorie.objects.get_or_create(nom="Autres")
                facture.categorie = autres

            facture.save()
            return redirect('facture_cree')
    else:
        form = FactureForm()

    return render(request, 'factures/creer_facture.html', {'form': form})

def facture_cree(request):
    return render(request, 'factures/facture_cree.html')

def modifier_facture(request, facture_id):
    facture = get_object_or_404(Facture, pk=facture_id)

    if request.method == 'POST':
        form = FactureForm(request.POST, instance=facture)
        if form.is_valid():
            form.save()
            return redirect('facture_cree')  # ou vers une page de confirmation
    else:
        form = FactureForm(instance=facture)

    return render(request, 'factures/modifier_facture.html', {'form': form, 'facture': facture})

def liste_factures(request):
    client_id = request.GET.get('client')
    if client_id:
        factures = Facture.objects.filter(client__id=client_id)
    else:
        factures = Facture.objects.all()
    
    clients = Client.objects.all() 
    return render(request, 'factures/liste_factures.html', {
        'factures': factures,
        'clients': clients,
        'client_id': int(client_id) if client_id else None,
    })


def supprimer_facture(request, facture_id):
    facture = get_object_or_404(Facture, pk=facture_id)
    
    if request.method == 'POST':
        facture.delete()
        return redirect('liste_factures')

    return render(request, 'factures/confirmer_suppression.html', {'facture': facture})

def details_facture(request, facture_id):
    facture = get_object_or_404(Facture, pk=facture_id)
    return render(request, 'factures/details_facture.html', {'facture': facture})

