from django.db import models

# Create your models here.

class AreaDeAtuacao(models.Model):

    nome = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nome

class Fornecedor(models.Model):

    CHOICES = (
        ('l', 'Livros e Periodicos'),
        ('e', 'Equipamentos Eletronicos'),
        ('r', 'Restaurantes'),
        ('f', 'Ferragens'),
        ('t', 'Transpostes'),
        ('v', 'Veiculos'),
        ('g', 'Grafica'),
    )
    razao = models.CharField(max_length=200,verbose_name=u'Razao Social')
    fantasia = models.CharField(blank=True,max_length=200)
    cnpj = models.IntegerField(blank=True,max_length=14,verbose_name=u'CNPJ/CPF')
    endereco = models.CharField(blank=True,max_length=200)    
    cidade = models.CharField(blank=True,max_length=200)
    estado = models.CharField(blank=True,max_length=200)
    telefone = models.CharField(max_length=12,verbose_name=u'Telefone',help_text="xxxxxxxxxx")
    fax = models.CharField(blank=True,max_length=12,verbose_name=u'Fax:(Opcional)')
    email = models.EmailField(blank=True,max_length=200)
    area = models.ForeignKey(AreaDeAtuacao)
    site = models.URLField(blank=True,max_length=200)
    obs = models.TextField(blank=True,verbose_name=u'Observacao')
    data = models.DateField(auto_now=True)
    
    def __unicode__(self):
        return self.razao




