from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms




class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name','username', 'password1', 'password2')
