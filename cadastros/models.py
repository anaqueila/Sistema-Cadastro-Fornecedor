from django.db import models

# Create your models here.

class Fornecedor(models.Model):

    GENDER_CHOICES = (
        ('l', 'Livros e Periodicos'),
        ('e', 'Equipamentos Eletronicos'),
        ('r', 'Restaurantes'),
        ('f', 'Ferragens'),
        ('t', 'Transpostes'),
        ('v', 'Veiculos'),
        ('g', 'Grafica'),
    )
    razao = models.CharField(blank=True,max_length=200,verbose_name=u'Razao Social')
    fantasia = models.CharField(max_length=200)
    cnpj = models.IntegerField(blank=True,max_length=14,verbose_name=u'CNPJ/CPF')
    cidade = models.CharField(blank=True,max_length=200)
    endereco = models.CharField(blank=True,max_length=200)
    telefone = models.CharField(max_length=12,verbose_name=u'Telefone')
    fax = models.CharField(blank=True,max_length=12,verbose_name=u'Fax:(Opcional)')
    email = models.EmailField(blank=True,max_length=200)
    area = models.CharField(blank=True,max_length=1, choices=GENDER_CHOICES,verbose_name=u'Area de atuacao')
    site = models.URLField(blank=True,max_length=200)
    obs = models.TextField(blank=True,verbose_name=u'Observacao')
    data = models.DateField(auto_now=True)
    
    def __unicode__(self):
        return self.razao


