from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    TIPO_PESSOA_CHOICES = [
        ('F', 'Pessoa Física'),
        ('J', 'Pessoa Jurídica'),
    ]

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    tipo_pessoa = models.CharField(max_length=1, choices=TIPO_PESSOA_CHOICES)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=14)
    cep = models.CharField(max_length=9)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
    
class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    ano_publicacao = models.PositiveIntegerField()

    def __str__(self):
        return self.titulo