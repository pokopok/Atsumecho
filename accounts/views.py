from django.shortcuts import render
import os
from django.views.generic.edit import CreateView
from .forms import CreateForm, UserLoginForm
from django.contrib.auth.views import LoginView, LogoutView


class CreateUserView(CreateView):
    template_name = os.path.join('accounts', 'create_user.html')
    form_class = CreateForm

class UserLoginView(LoginView):
    template_name = os.path.join('accounts', 'user_login.html')
    authentication_form = UserLoginForm

class UserLogoutView(LogoutView):
    pass