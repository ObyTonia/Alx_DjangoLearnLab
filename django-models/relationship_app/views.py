from django.shortcuts import render

# Create your views here.
from .models import Book  # Import your Book model

def list_books(request):
  books = Book.objects.all()  # Fetch all books from database
  context = {'books': books}  # Create a context dictionary
  return render(request, 'relationship_app/list_books.html', context)  # Render template with context


from django.views.generic.detail import DetailView
from .models import Library

class LibraryDetailView(DetailView):
  model = Library  # Specify the model for the view
  template_name = 'relationship_app/library_detail.html'  # Set the template for rendering

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['books'] = self.object.books.all()  # Access library's books
    return context

from django.urls import path
from . import views

urlpatterns = [
  path('books/', views.list_books, name='list_books'),
  path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]