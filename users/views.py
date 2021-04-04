from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.


from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from users.forms import LoginForm, RegisterForm


#from .forms import UserProfileForm


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('home')

class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

@login_required
def home(request):
    return render(request, 'home.html')
