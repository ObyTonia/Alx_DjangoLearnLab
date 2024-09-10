from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .views import add_comment, edit_comment, delete_comment


urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
    path('profile/', views.user_profile, name='profile'),
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/comments/new/', add_comment, name='add_comment'),
    path('comment/<int:pk>/update/', edit_comment, name='edit_comment'),
    path('comment/<int:pk>/delete/', delete_comment, name='delete_comment'),
    path('tags/<slug:tag_name>/', views.tag_posts, name='tag_posts'),
    path('search/', views.search, name='search'),
]