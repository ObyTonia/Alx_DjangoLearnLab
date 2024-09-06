```python
from bookshelf.models import Book

# Create a new Book instance
book = Book.objects.create (title="1984", author="George Orwell", publication_year=1949)
book.save()

Expected Output: [{'id': 1, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949}]
