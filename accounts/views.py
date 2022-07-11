from django.shortcuts import render
from django.views.generic.base import TemplateView
import os

class HomeView(TemplateView):
    template_name = os.path.join('accounts', 'home.html')
