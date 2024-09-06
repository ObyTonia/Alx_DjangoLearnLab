from django.urls import path
from .views import BookListView, BookDetailView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),  # Handles GET (list) and POST (create)
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),  # Handles GET (retrieve), PUT (update), DELETE (delete)
]