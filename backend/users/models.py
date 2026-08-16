from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    """Custom User model fields """

    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Administrator',
        SHAREHOLDER = 'SHAREHOLDER', 'Shareholder'
        MANAGER = 'MANAGER', 'Manager'
        DOCTOR = 'DOCTOR', 'Doctor'
        NURSE = 'NURSE', 'Nurse'
        RECEPTIONIST = 'RECEPTIONIST', 'Receptionist',
        GUARD = 'GUARD', 'Security Guard'
        PATIENT = 'PATIENT', 'Patient'

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=200)
    bio = models.TextField(blank = True)
    email = models.EmailField(unique = True)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=175)
    date_of_birth = models.DateField(blank=True, null=True)
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.PATIENT
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.name