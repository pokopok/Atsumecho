from django.urls import path
from . import views

app_name = 'goshuin_books'

urlpatterns = [
    path('create_book', views.GoshuinBookCreateView.as_view(), name='create_book'),
    path('list_book', views.GoshuinBookListView.as_view(), name='list_book'),
    path('book/<int:book>', views.GoshuinListView.as_view(), name='book'),
]