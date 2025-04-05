from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Perfil

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)
    nome = forms.CharField(max_length=100)
    sobrenome = forms.CharField(max_length=100)
    tipo_pessoa = forms.ChoiceField(choices=Perfil.TIPO_PESSOA_CHOICES, widget=forms.RadioSelect)
    data_nascimento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    cpf = forms.CharField(max_length=14)
    cep = forms.CharField(max_length=9)
    endereco = forms.CharField(max_length=200)
    telefone = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',
                  'nome', 'sobrenome', 'tipo_pessoa', 'data_nascimento',
                  'cpf', 'cep', 'endereco', 'telefone']
