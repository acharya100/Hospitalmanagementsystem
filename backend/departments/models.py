from django.db import models
import uuid
from users.models import User
from hospitals.models import Hospital
# Create your models here.

class Department(models.Model):
    """custom department model fields"""
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=175)
    description = models.TextField(blank = True)
    doctors = models.ManyToManyField(User, related_name='departments')
    hospital = models.ForeignKey(
        Hospital, on_delete=models.PROTECT,
        related_name='departments'
    )
    is_available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name