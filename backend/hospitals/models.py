from django.db import models

import uuid
from users.models import User
# Create your models here.

class Hospital(models.Model):
    """ custom hospital model fields """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=230)
    description = models.TextField(blank = True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank = True)
    address = models.CharField(max_length=50, blank=True)
    shareholders = models.ManyToManyField(User, related_name="hospitals")
    established_date = models.DateField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    is_open = models.BooleanField(default = True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name