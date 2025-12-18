from django.contrib import admin
from .models import Observateur, Prefecture, Commune, Region


admin.site.index_title = "Manager"
admin.site.site_header = "Gestion des Ressources Humaines"

admin.site.register(Region)

class AdminPrefecture(admin.ModelAdmin):
    list_display = ('region', 'prefecture')
    search_fields = ('region', 'prefecture')

admin.site.register(Prefecture)


class AdminCommune(admin.ModelAdmin):
    list_display = ('prefecture', 'commune')
    search_fields = ('prefecture', 'commune')

admin.site.register(Commune, AdminCommune)


class AdminObservateur(admin.ModelAdmin):
    list_display = ('region', 'prefecture', 'commune', 'telephone', 'prenom', 'nom', 'telephone')
    search_fields = ('region', 'prefecture', 'commune', 'telephone', 'prenom', 'nom', 'telephone')

admin.site.register(Observateur, AdminObservateur)