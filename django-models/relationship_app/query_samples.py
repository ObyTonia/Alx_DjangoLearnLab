from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author

def query_all_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books

# List all books in a library
def list_all_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books

# Retrieve the librarian for a library
def retrieve_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    return librarian


# Example usage
author_name = "John Doe"
library_name = "Central Library"

books = query_all_books_by_author(author_name)
library_books = list_all_books_in_library(library_name)
librarian = retrieve_librarian_for_library(library_name)

print(f"Books by {author_name}:")
for book in books:
    print(f"- {book.title}")

print(f"\nBooks in {library_name}:")
for book in library_books:
    print(f"- {book.title}")

print(f"\nLibrarian for {library_name}: {librarian.name}")