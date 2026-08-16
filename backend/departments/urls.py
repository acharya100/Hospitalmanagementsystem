from django.urls import path
from departments.views import DepartmentListAPIView, DepartmentDetailAPIView

urlpatterns = [
    path('departments/', DepartmentListAPIView.as_view(), name='department-list'),
    path('departments/<uuid:pk>/', DepartmentDetailAPIView.as_view(), name= 'department-detail')
]
