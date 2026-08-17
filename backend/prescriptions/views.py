from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status

from prescriptions.models import Prescription, PrescriptionItem
from prescriptions.serializers import PrescriptionSerializer, PrescriptionItemSerializer
# Create your views here.

class PrescriptionListAPIView(APIView):
    def get(self, request):
        prescriptions = Prescription.objects.all()
        serializer = PrescriptionSerializer(prescriptions, many = True)

        return Response(serializer.data)

    def post(self, request):
        serializer = PrescriptionSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PrescriptionDetailAPIView(APIView):
    def get(self, request, pk):
        prescription = get_object_or_404(Prescription, id=pk)
        serializer = PrescriptionSerializer(prescription)

        return Response(serializer.data)

    def put(self, request,pk):
        prescription = get_object_or_404(Prescription, id=pk)
        serializer = PrescriptionSerializer(prescription, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        prescription = get_object_or_404(Prescription, id=pk)
        prescription.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)



class PrescriptionItemListAPIView(APIView):
    def get(self, request):
        prescriptionitems = PrescriptionItem.objects.all()
        serializer = PrescriptionItemSerializer(prescriptionitems, many = True)

        return Response(serializer.data)

    def post(self, request):
        serializer = PrescriptionItemSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PrescriptionItemDetailAPIView(APIView):
    def get(self, request, pk):
        prescriptionitem = get_object_or_404(PrescriptionItem, id=pk)
        serializer = PrescriptionItemSerializer(prescriptionitem)

        return Response(serializer.data)

    def put(self, request,pk):
        prescriptionitem = get_object_or_404(PrescriptionItem, id=pk)
        serializer = PrescriptionItemSerializer(prescriptionitem, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        prescriptionitem = get_object_or_404(PrescriptionItem, id=pk)
        prescriptionitem.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)