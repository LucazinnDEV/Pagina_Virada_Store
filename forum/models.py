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

from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='livros/')
    preco = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.titulo

