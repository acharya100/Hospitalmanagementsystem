from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from departments.models import Department
from departments.serializers import DepartmentSerializer
# Create your views here.

class DepartmentListAPIView(APIView):
    def get(self, request):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many = True)

        return Response(serializer.data)

    def post(self, request):
        serializer = DepartmentSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class DepartmentDetailAPIView(APIView):
    def get(self, request, pk):
        department = get_object_or_404(Department, id=pk)
        serializer = DepartmentSerializer(department)

        return Response(serializer.data)

    def put(self, request,pk):
        department = get_object_or_404(Department, id=pk)
        serializer = DepartmentSerializer(department, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        department = get_object_or_404(Department, id=pk)
        department.delete()

        return Response(status=204)