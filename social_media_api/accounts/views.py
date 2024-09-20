from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import UserSerializer
from django.contrib.auth import get_user_model

# User registration view
class RegisterView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

# Custom token-based login view
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })

    " Views to allow users to follow and unfollow other users."

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import CustomUser

class FollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()  # Use this for filtering users

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(self.get_queryset(), id=user_id)
        request.user.following.add(user_to_follow)
        return Response({"detail": "Followed successfully"}, status=status.HTTP_200_OK)

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()  # Use this for filtering users

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(self.get_queryset(), id=user_id)
        request.user.following.remove(user_to_unfollow)
        return Response({"detail": "Unfollowed successfully"}, status=status.HTTP_200_OK)
    

"Create a feed view in the posts app to retrieve posts from users that the current user follows"
#feed view 
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer

class FeedView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        followed_users = user.following.all()
        return Post.objects.filter(author__in=followed_users).order_by('-created_at')
