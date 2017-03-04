from django.db import models

# Create your models here.

class Uf(models.Model):
	sigla = models.CharField(max_length=2, primary_key=True)
	nome = models.CharField(max_length=60)

class Municipio(models.Model):
	uf = models.ForeignKey(Uf, on_delete=models.CASCADE)	
	nome = models.CharField(max_length=60)

class TipoGestao(models.Model):
	nome = models.CharField(max_length=60)
class Estabelecimento(models.Model):
	simNao = (('S', 'Sim'),('N', 'Não'))
	cnes = models.CharField(max_length=7, primary_key=True)
	nome = models.CharField(max_length=60)
	razaoSocial = models.CharField(max_length=100)
	municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)	
	tipoGestao = models.ForeignKey(TipoGestao, on_delete=models.CASCADE)
	atendeSus = models.CharField(max_length=1, choices=simNao)
