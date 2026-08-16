from django.db import models

import uuid
from users.models import User
from departments.models import Department
# Create your models here.

class Appointment(models.Model):
    """ custom appointment model fields """
    class Booking(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        CONFIRMED = 'CONFIRMED', 'Confirmed'
        COMPLETED = 'COMPLETED', 'Completed'
        CANCELLED = 'CANCELLED', 'Cancelled'
        ABSENT = 'ABSENT', 'Absent'

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    patient = models.ForeignKey(
        User, on_delete=models.PROTECT,
        related_name='patient_appointments'
    )
    doctor = models.ForeignKey(
        User,on_delete=models.PROTECT,
        related_name='doctor_appointments')
    department = models.ForeignKey(
        Department, on_delete=models.PROTECT,
        related_name='appointments'
    )
    booking = models.CharField(
        max_length=20,
        choices=Booking.choices,
        default=Booking.PENDING
    )

    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    appointment_fee = models.DecimalField(max_digits=12, decimal_places=2)
    appointment_description = models.TextField(blank = True) 
    appointment_number = models.PositiveIntegerField(unique=True)
    room_number = models.CharField(max_length=20, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Appointment Number {self.appointment_number} for {self.patient.name}"
