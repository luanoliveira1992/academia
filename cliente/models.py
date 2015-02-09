from django.core.urlresolvers import reverse
from django.db import models
from bsct.models import BSCTModelMixin

# Create your models here.


class EnderecoUsuario(BSCTModelMixin,models.Model):
    codigo = models.AutoField(primary_key=True)
    logradouro = models.CharField(max_length = 100)
    numero = models.IntegerField()
    complemento = models.TextField(max_length= 200)
    
class ClienteSaude(BSCTModelMixin,models.Model):
    codigo = models.AutoField(primary_key=True)
    peso = models.DecimalField(decimal_places=2,max_digits=5)
    altura = models.DecimalField(decimal_places=2,max_digits=5)
    diametroBraco =        models.DecimalField(decimal_places=2,max_digits=5)
    diametroCintura = models.DecimalField(decimal_places=2,max_digits=5)
    diametroPerna = models.DecimalField(decimal_places=2,max_digits=5)
    horasMalharDia = models.IntegerField(max_length=24)
    diasMalharSemana = models.IntegerField(max_length=7)

    
    
class Cliente( BSCTModelMixin, models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50,default="")
    cpf = models.CharField(max_length=11,default="")
    rg = models.CharField(max_length=20,default="")
    endereco = models.ForeignKey(EnderecoUsuario)
    saude = models.ForeignKey(ClienteSaude)
    dataPagamento = models.IntegerField(max_length=31,default=5)
    email = models.EmailField(max_length=50,default="")
    telefone = models.CharField(max_length=50,default="")
    redeSocial = models.TextField(max_length=500,default="")
    
    def codigo_detail( self ):
        return 'CODIGO_%d' % ( self.codigo )

    def __unicode__( self ):
        return '%s' % ( self.name )
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
    


    
    

    
