``` Python 

#delete book
book.delete()

books = Book.objects.all()
if books.exists():
    print("Book still exists!")
else:
    print("Book deleted successfully!")

Expected Output: Book deleted succefully