from django.shortcuts import render, redirect
from django.views.generic import View
from login.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

class LoginView(View):
    def get(self, request):
        template = 'login/dashboard.html'
        form = LoginForm(request.POST or None)

        data = {
            'form': form
        }

        return render(request, template, data)
