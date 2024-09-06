from django.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book, Author
from .serializers import BookSerializer

class BookAPITests(APITestCase):
    def setUp(self):
        self.client.login = APIClient()
        
        # Create an Author instance
        self.author = Author.objects.create(name='Test Author')
        
        self.book_data = {
            'title': 'Test Book',
            'author': self.author.id,  # Use the Author instance ID
            'publication_year': 2024
        }
        
        self.book = Book.objects.create(**self.book_data)
        self.book_url = f'/api/books/{self.book.id}/'
        self.list_url = '/api/books/'

    def test_create_book(self):
        response = self.client.post(self.list_url, self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)  # 1 from setUp + 1 new

    def test_get_book(self):
        response = self.client.get(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book_data['title'])
        

    def test_update_book(self):
        update_data = {'title': 'Updated Book Title'}
        response = self.client.put(self.book_url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book Title')

    def test_delete_book(self):
        response = self.client.delete(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books(self):
        response = self.client.get(self.list_url, {'title': 'Test Book'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_search_books(self):
        response = self.client.get(self.list_url, {'search': 'Test'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_ordering_books(self):
        response = self.client.get(self.list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['title'], 'Test Book')