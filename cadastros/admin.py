from django import forms
from models import Fornecedor, AreaDeAtuacao
from django.contrib import admin
from django.contrib.localflavor.br.forms import BRCNPJField,BRPhoneNumberField

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
    telefone = BRPhoneNumberField(help_text="o campo deve ser preenchido da seguinte maneira: xxxxxxxxxx")
    fax = BRPhoneNumberField(help_text="o campo deve ser preenchido da seguinte maneira: xxxxxxxxxx")
    #area = forms.ModelChoiceField(
       # queryset = AreaDeAtuacao.objects.all(), empty_label=None,   
    #)

class FornAdmin(admin.ModelAdmin):
    search_fields = ['razao','fantasia','area','obs','cidade','endereco']
    list_display = ['razao','fantasia','area','telefone','fax','site','data']
    list_filter = ['area']
    date_hierarchy = 'data'
    list_display_links = ['razao']
    ordering = ['data']
    list_per_page = 5
    form = FornecedorForm

class AreaAdmin(admin.ModelAdmin):
    ordering = ['nome']

admin.site.register(Fornecedor, FornAdmin)

admin.site.register(AreaDeAtuacao,AreaAdmin)


