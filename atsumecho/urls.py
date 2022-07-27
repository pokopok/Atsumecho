from django.urls import path
from . import views

app_name = 'atsumecho'

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('create_book', views.BookCreateView.as_view(), name='create_book'),
    path('list_book', views.BookListView.as_view(), name='list_book'),
    path('book/<int:book_id>', views.RecordListView.as_view(), name='book'),
    path('add_record/<int:book_id>', views.RecordAddView.as_view(), name='add_record'),
    path('delete_book/<int:pk>', views.BookDeleteView.as_view(), name='delete_book'),
    path('delete_record/<int:pk>', views.RecordDeleteView.as_view(), name='delete_record'),
    path('update_book/<int:pk>', views.BookUpdateView.as_view(), name='update_book'),
    path('update_record/<int:pk>', views.RecordUpdateView.as_view(), name='update_record'),
]