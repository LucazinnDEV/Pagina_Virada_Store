from django.db import models

class Pergunta(models.Model):
    titulo = models.CharField(max_length=200)
    detalhe = models.TextField()
    tentativa = models.TextField()
    data_criacao = models.DateTimeField()

class Resposta(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    texto = models.TextField()
    data_criacao = models.DateTimeField()
