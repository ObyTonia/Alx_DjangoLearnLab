# admin_view.py

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda user: user.profile.role == 'Admin')
def admin_view(request):
    # Admin-specific content here
    return render(request, 'admin_template.html')