from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('create_user/', views.CreateUserView.as_view(), name='create_user'),
]