from django.db import models

import uuid
from users.models import User
from hospitals.models import Hospital
# Create your models here.

class Review(models.Model):
    """ custom review model fields """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    patient = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='reviews'
    )
    hospital = models.ForeignKey(
        Hospital, on_delete=models.CASCADE,
        related_name='reviews'
    )
    rating = models.FloatField()
    comment = models.TextField(blank= True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.rating} star rating for {self.hospital.name}"