from django.urls import path
from prescriptions.views import PrescriptionListAPIView, PrescriptionDetailAPIView, PrescriptionItemListAPIView, PrescriptionItemDetailAPIView

urlpatterns = [
    path('prescriptions/', PrescriptionListAPIView.as_view(), name = 'prescription-list'),
    path('prescriptions/<uuid:pk>/', PrescriptionDetailAPIView.as_view(), name= 'prescription-detail'),

    path('prescriptionitems/', PrescriptionItemListAPIView.as_view(), name='prescriptionitem-list'),
    path('prescriptionitems/<uuid:pk>/', PrescriptionItemDetailAPIView.as_view(), name='prescriptionitem-detail')
]
