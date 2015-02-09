from django.db import models

# Create your models here.
class TipoUsuario(models.Model):
	codigo = models.AutoField(primary_key=True)
	descricao = models.CharField(max_length=50)
	cadastro = models.DateTimeField(auto_now=True)

	def __str__(self):
                return self.descricao.encode('ascii','ignore')



class Usuario(models.Model):
	codigo = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	senha = models.CharField(max_length=10)
	tipo = models.ForeignKey(TipoUsuario)


	def __str__(self):
                return self.nome
	
		

