from django.db import models
import uuid
# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=200, null= True, blank=True)
    email = models.EmailField(max_length=200, null= True, blank=True)
    subject = models.CharField(max_length=200, null= True, blank=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False, null= True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.subject
