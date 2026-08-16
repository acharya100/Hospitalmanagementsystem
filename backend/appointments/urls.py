from django.urls import path
from appointments.views import AppointmentListAPIView, AppointmentDetailAPIView


urlpatterns = [
    path('appointments/', AppointmentListAPIView.as_view(), name='appointment-list'),
    path('appointments/<uuid:pk>/', AppointmentDetailAPIView.as_view(), name= 'appointment-detail')
]
