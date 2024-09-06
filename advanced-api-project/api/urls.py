from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('books/',BookListView.as_view(), name='book-list'), # Handles GET (list) and POST (create)
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'), # Handles GET (retrieve), PUT (update), DELETE (delete)
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]