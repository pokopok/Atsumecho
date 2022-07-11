from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .forms import CreateForm
import os

class HomeView(TemplateView):
    template_name = os.path.join('accounts', 'home.html')

class CreateUserView(CreateView):
    template_name = os.path.join('accounts', 'create_user.html')
    form_class = CreateForm