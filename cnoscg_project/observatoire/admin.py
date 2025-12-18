from django.contrib import admin
from .models import Observateur

# Register your models here.


admin.site.index_title = "Manager"
admin.site.site_header = "Gestion des Observateurs du CNOSCG"

class AdminObservateur(admin.ModelAdmin):
    list_display = ('region', 'prefecture', 'commune', 'telephone', 'prenom', 'nom', 'telephone', 'picture')
    search_fields = ('telephone', 'prenom', 'nom', 'prefecture')


admin.site.register(Observateur, AdminObservateur)