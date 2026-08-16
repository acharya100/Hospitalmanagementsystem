from django.urls import path
from hospitals.views import HospitalListAPIView, HospitalDetailAPIView

urlpatterns = [
    path('hospitals/', HospitalListAPIView.as_view(), name='hospital-list'),
    path('hospitals/<uuid:pk>/', HospitalDetailAPIView.as_view(), name='hospital-detail')
]
