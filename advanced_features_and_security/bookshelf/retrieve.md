```python
from bookshelf.models import Book
# Retrieve the book
book = Book.objects.get(title="1984")
print(book)

Expected Output: 1984 by George Orwell (1949)
