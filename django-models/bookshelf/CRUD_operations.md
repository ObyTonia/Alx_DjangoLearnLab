```python
from bookshelf.models import Book

# Create a new Book instance
book = Book.objects.create (title="1984", author="George Orwell", publication_year=1949)
book.save()

Expected Output: [{'id': 1, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949}]

# Retrieve the book
book = Book.objects.get(title="1984")
print(book)

Expected Output: 1984 by George Orwell (1949)

#Update Book
book.title = "Nineteen Eighty-Four"
book.save()

print(book.title)

Expected Output: Nineteen Eighty-Four

#delete book
book.delete()

books = Book.objects.all()
if books.exists():
    print("Book still exists!")
else:
    print("Book deleted successfully!")

Expected Output: Book deleted succefully