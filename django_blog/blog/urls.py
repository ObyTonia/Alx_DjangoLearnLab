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
    path('<int:post_pk>/comments/new/', views.CommentCreateView.as_view(), name='comment_new'),
    path('<int:post_pk>/comments/<int:comment_pk>/edit/', views.CommentUpdateView.as_view(), name='comment_edit'),
    path('<int:post_pk>/comments/<int:comment_pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
]