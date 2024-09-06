from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book
from .serializers import BookSerializer

class BaseTest(APITestCase):
    def setUp(self):
        self.book_data = {
            'title': 'Test Book',
            'author': 'Test Author',
            'publication_year': 2023,
        }
def test_create_book(self):
    url = reverse('book-list')
    data = self.book_data
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Book.objects.count(), 1)
    self.assertEqual(Book.objects.get().title,   
 data['title'])
    
def test_retrieve_book(self):
    # Create a book first
    book = Book.objects.create(**self.book_data)
    url = reverse('book-detail', kwargs={'pk': book.pk})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    serializer_data = BookSerializer(book).data
    self.assertEqual(response.data, serializer_data)

def test_update_book(self):
    # Create a book
    book = Book.objects.create(**self.book_data)
    url = reverse('book-detail', kwargs={'pk': book.pk})
    data = {'title': 'Updated Title'}
    response = self.client.put(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    book.refresh_from_db()
    self.assertEqual(book.title, data['title'])

def test_delete_book(self):
    # Create a book
    book = Book.objects.create(**self.book_data)
    url = reverse('book-detail', kwargs={'pk': book.pk})
    response = self.client.delete(url)
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    self.assertEqual(Book.objects.count(),   
 0)