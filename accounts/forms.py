import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class SignUpForm(UserCreationForm):
    full_name = forms.CharField(
        label="Nome Completo",
        max_length=150,
        required=True
    )

    class Meta:
        model = User
        fields = ['username', 'full_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Usuário'
        self.fields['username'].help_text = ''
        
        # Limpa o texto de ajuda padrão das senhas
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
