from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, filters
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

      # Add filtering capability
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

"Create a feed view in the posts app to retrieve posts from users that the current user follows"
#feed view 
from rest_framework import generics
from rest_framework import permissions
from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response

class UserFeedView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serialized_posts = PostSerializer(posts, many=True)
        return Response(serialized_posts.data)
    
"Create Views for Liking and Unliking Posts:"
# posts/views.py
from rest_framework import generics
from django.http import JsonResponse
from .models import Post, Like
from notifications.models import Notification

def like_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)
    post = generics.get_object_or_404(Post, pk=pk)
    user = request.user
    if Like.objects.get_or_create(user=request.user, post=post).exists():
        return JsonResponse({'error': 'You already liked this post.'}, status=400)
    like = Like.objects.create(user=user, post=post)
    # Create notification
    Notification.objects.create(recipient=post.author, actor=user, verb='liked', target=post)
    return JsonResponse({'message': 'Post liked.'}, status=200)

def unlike_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)
    user = request.user
    like = Like.objects.filter(user=user, post=post)
    if not like.exists():
        return JsonResponse({'error': 'You have not liked this post.'}, status=400)
    like.delete()
    return JsonResponse({'message': 'Post unliked.'}, status=200)
