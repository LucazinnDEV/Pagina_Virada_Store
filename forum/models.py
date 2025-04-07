from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

class Perfil(models.Model):
    TIPO_PESSOA_CHOICES = [
        ('F', 'Pessoa Física'),
        ('J', 'Pessoa Jurídica'),
    ]

    usuario = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    tipo_pessoa = models.CharField(max_length=1, choices=TIPO_PESSOA_CHOICES)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=14, unique=True)
    cep = models.CharField(max_length=9)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.URLField(blank=True)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    imagem = models.ImageField(
        upload_to='livros/',
        validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])],
        blank=True, null=True
    )
    autor = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    vendas = models.PositiveIntegerField(default=0)
    recomendado = models.BooleanField(default=False)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='livros',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.titulo