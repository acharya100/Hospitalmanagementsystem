from django.db import models

import uuid
from users.models import User
from appointments.models import Appointment

# Create your models here.

class Prescription(models.Model):
    """ custom prescription model fields """
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pending',
        PROCESSING = 'PROCESSING', 'Processing',
        READY = 'READY', 'Ready'
        RECEIVED = 'RECEIVED', 'Received'
        CANCELLED = 'CANCELLED', 'Cancelled'

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
        )
    appointment = models.OneToOneField(
        Appointment, on_delete=models.PROTECT,
        related_name='prescription'
    )
    description = models.TextField(blank=True)
    patient = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='prescriptions')

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING 
    )
    prescription_date = models.DateField()
    prescription_time = models.TimeField()
    total_price = models.DecimalField(max_digits=15, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Prescription for {self.patient.name}"

    
class PrescriptionItem(models.Model):
    """ custom prescription item model fields """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    prescription = models.ForeignKey(
        Prescription, on_delete=models.CASCADE,
        related_name='prescriptionitems',
    )
    medicine_name = models.CharField(max_length=200)
    unit_price = models.DecimalField(max_digits=12, decimal_places=2)
    quantity = models.PositiveBigIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quantity} X {self.medicine_name}"