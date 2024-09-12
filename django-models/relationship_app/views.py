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

#customization
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Custom registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})



# Role views
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship/member_view.html')

