from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

# Custom user serializer for user registration
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'password', 'email', 'bio', 'profile_picture']  # Add other fields if necessary
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Create a new user using the create_user method
        user = get_user_model().objects.create_user(**validated_data)
        
        # Create the token for the new user
        Token.objects.create(user=user)
        
        return user
