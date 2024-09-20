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
# Add like_post and unlike_post views to handle post likes and unlikes:

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Like

@api_view(['POST'])
def like_post(request, pk):
    post = Post.objects.get(pk=pk)
    user = request.user

    # Check if the post is already liked by the user
    if Like.objects.filter(user=user, post=post).exists():
        return Response({'message': 'Post already liked'}, status=status.HTTP_400_BAD_REQUEST)

    # Create a like
    Like.objects.create(user=user, post=post)
    create_notification(actor=user, recipient=post.user, verb='liked your post', target=post)

    return Response({'message': 'Post liked'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def unlike_post(request, pk):
    post = Post.objects.get(pk=pk)
    user = request.user
