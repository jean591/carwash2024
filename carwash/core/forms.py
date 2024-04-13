from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class LoginForm(AuthenticationForm):
    pass
      

class RegisterForm(UserCreationForm):
    
    email = forms.EmailField(label='Correo electronico')
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    username=forms.CharField(label='Nombre de Usuario')
    password1=forms.CharField(label='Contraseña')
    password2=forms.CharField(label='Confirmar Contraseña')

    
    

    class Meta:
        model = User
        fields =['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    
