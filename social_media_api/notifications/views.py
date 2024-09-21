from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Notification

@api_view(['GET'])
def user_notifications(request):
    user = request.user
    notifications = Notification.objects.filter(recipient=user, read=False)
    data = [{
        "actor": n.actor.username,
        "verb": n.verb,
        "target": str(n.target),
        "timestamp": n.timestamp
    } for n in notifications]
    return Response(data)
