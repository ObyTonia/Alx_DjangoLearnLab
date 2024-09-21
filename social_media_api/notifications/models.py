from django.db import models

# Create your models here.
"Notification Model (notifications app):"

from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

User = get_user_model()

class Notification(models.Model):
    recipient = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
    actor = models.ForeignKey(User, related_name='notifications_sent', on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)
    target_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, null=True)
    target_object_id = models.PositiveIntegerField(blank=True, null=True)
    target = GenericForeignKey('target_content_type', 'target_object_id')
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.actor} {self.verb} {self.target}"

    class Meta:
        ordering = ['-timestamp']  # Newest notifications first