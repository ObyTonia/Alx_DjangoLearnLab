from django.urls import path
from .views import BookList
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]

"ROUTERSETUP"
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),  # Includes all routes registered with the router
]