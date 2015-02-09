from django.db import models

# Create your models here.


class Exercicio(models.Model):
    codigo = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=50)
    riscoSaude = models.BooleanField(default=False)
    doencasEvitar = models.TextField(max_length=500)
    
    def __str__(self):
            return self.descricao

class CategoriaAparelho(models.Model):
    codigo = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=50)
    exercicio = models.ForeignKey(Exercicio)
        
    def __str__(self):
                return self.descricao
    

    
class Aparelho(models.Model):
    codigo = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=50)
    categorias = models.ForeignKey(CategoriaAparelho)
    
    def __str__(self):
                return self.descricao
     

                                 
                                   
                                   
                                   
                                   
                                   
