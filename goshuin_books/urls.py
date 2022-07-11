from django.urls import path
from . import views

app_name = 'goshuin_books'

urlpatterns = [
    path('create_book', views.GoshuinBookCreateView.as_view(), name='create_book'),
]