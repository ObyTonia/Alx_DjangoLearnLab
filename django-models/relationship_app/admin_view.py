# admin_view.py

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Check if the user has the 'Admin' role
def is_admin(user):
    return user.userprofile.role == 'Admin'

@user_passes_test(lambda user: user.profile.role == 'Admin')
def admin_view(request):
    # Admin-specific content here
    return render(request, 'admin_view.html')