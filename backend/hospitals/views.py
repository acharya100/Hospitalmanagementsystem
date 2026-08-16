from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from hospitals.models import Hospital
from hospitals.serializers import HospitalSerializer
# Create your views here.

class HospitalListAPIView(APIView):
    def get(self, request):
        hospitals = Hospital.objects.all()
        serializer = HospitalSerializer(hospitals, many = True)

        return Response(serializer.data)

    def post(self, request):
        serializer = HospitalSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class HospitalDetailAPIView(APIView):
    def get(self, request, pk):
        hospital = get_object_or_404(Hospital, id=pk)
        serializer = HospitalSerializer(hospital)

        return Response(serializer.data)

    def put(self, request,pk):
        hospital = get_object_or_404(Hospital, id=pk)
        serializer = HospitalSerializer(hospital, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        hospital = get_object_or_404(Hospital, id=pk)
        hospital.delete()

        return Response(status=204)