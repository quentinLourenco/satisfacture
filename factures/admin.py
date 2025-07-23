from django.contrib import admin
from .models import Facture, Categorie, Client

@admin.action(description="Marquer les factures comme payées")
def marquer_comme_payees(modeladmin, request, queryset):
    queryset.update(payee=True)

@admin.register(Facture)
class FactureAdmin(admin.ModelAdmin):
    list_display = ('titre', 'client', 'categorie', 'montant', 'date', 'payee')
    list_filter = ('client', 'categorie', 'payee')
    search_fields = ('titre', 'client__nom')
    actions = [marquer_comme_payees]  # 👈 Ajoute l'action ici

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('nom',)
