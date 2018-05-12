# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.views.generic import TemplateView
from django.conf import settings
from django.contrib.auth.models import User
from .forms import UserForm

def home(request):
    return render(request, 'connexion/home.html', {})



class LoginView(TemplateView):
  template_name = 'connexion/index.html'
  def post(self, request, **kwargs):
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        login(request, user)
        return HttpResponseRedirect('home')
        return render(request, self.template_name , {'user':user})

class LogoutView(TemplateView):
  template_name = 'connexion/index.html'
  def get(self, request, **kwargs):
    logout(request)
    return render(request, self.template_name)
# Create your views here.
