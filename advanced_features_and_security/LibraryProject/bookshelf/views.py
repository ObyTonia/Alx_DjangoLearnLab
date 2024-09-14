from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import Book

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    if request.method == 'POST':
        # logic to edit book
        pass
    return render(request, 'edit_book.html', {'book': book})