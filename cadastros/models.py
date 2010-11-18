from django.db import models

# Create your models here.

class AreaDeAtuacao(models.Model):

    nome = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nome

class Fornecedor(models.Model):

    razao = models.CharField(max_length=200,verbose_name=u'Razao Social',help_text="Campo Obrigatorio")
    fantasia = models.CharField(blank=True,max_length=200)
    contato = models.CharField(blank=True, max_length=100,verbose_name=u'Nome de Contato')
    cnpj = models.FloatField(verbose_name=u'CNPJ/CPF',help_text="Campo Obrigatorio")
    endereco = models.CharField(blank=True,max_length=200)    
    cidade = models.CharField(blank=True,max_length=200)
    estado = models.CharField(blank=True,max_length=200)
    telefone = models.CharField(max_length=12,verbose_name=u'Telefone',help_text="Campo Obrigatorio")
    fax = models.CharField(null=True,max_length=12,verbose_name=u'Fax:(Opcional)')
    email = models.EmailField(blank=True,max_length=200)
    area = models.ForeignKey(AreaDeAtuacao,help_text="Campo Obrigatorio")
    site = models.URLField(blank=True,max_length=200)
    obs = models.TextField(blank=True,verbose_name=u'Observacao')
    data = models.DateField(auto_now=True)
    
    def __unicode__(self):
        return self.razao




