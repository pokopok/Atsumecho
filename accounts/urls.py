from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('create_user/', views.CreateUserView.as_view(), name='create_user'),
    path('user_login/', views.UserLoginView.as_view(), name='user_login'),
    path('user_logout/', views.UserLogoutView.as_view(), name='user_logout'),
    ]