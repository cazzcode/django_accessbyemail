from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.


from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy

from users.forms import LoginForm


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('home')


@login_required
def home(request):
    return render(request, 'home.html')
