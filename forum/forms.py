from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuarioForm(UserCreationForm):
    nome_completo = forms.CharField(max_length=150, required=True)
    cpf = forms.CharField(max_length=14, required=True)
    endereco = forms.CharField(max_length=255, required=True)
    telefone = forms.CharField(max_length=15, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'nome_completo', 'cpf', 'endereco', 'telefone', 'email', 'password1', 'password2']
