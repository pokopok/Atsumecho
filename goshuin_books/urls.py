from django.urls import path
from . import views

app_name = 'goshuin_books'

urlpatterns = [
    path('create_book', views.GoshuinBookCreateView.as_view(), name='create_book'),
    path('list_book', views.GoshuinBookListView.as_view(), name='list_book'),
    path('book/<int:book_id>', views.GoshuinListView.as_view(), name='book'),
    path('add_goshuin/<int:book_id>', views.GoshuinAddView.as_view(), name='add_goshuin'),
    path('delete_book/<int:pk>', views.GoshuinBookDeleteView.as_view(), name='delete_book'),
    path('delete_goshuin/<int:pk>', views.GoshuinDeleteView.as_view(), name='delete_goshuin'),
    path('update_book/<int:pk>', views.GoshuinBookUpdateView.as_view(), name='update_book'),
    path('update_goshuin/<int:pk>', views.GoshuinUpdateView.as_view(), name='update_goshuin'),
]