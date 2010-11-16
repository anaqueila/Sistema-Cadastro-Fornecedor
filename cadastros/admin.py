from django import forms
from models import Fornecedor
from django.contrib import admin
from django.contrib.localflavor.br.forms import BRCNPJField,BRPhoneNumberField

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
    telefone = BRPhoneNumberField()

class FornAdmin(admin.ModelAdmin):
    search_fields = ['razao','fantasia','area','obs','cidade','endereco']
    list_display = ['razao','fantasia','area','telefone','site','data']
    list_filter = ['area']
    date_hierarchy = 'data'
    list_display_links = ['razao','fantasia']
    form = FornecedorForm


admin.site.register(Fornecedor, FornAdmin)

