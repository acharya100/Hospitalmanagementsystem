from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
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

            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

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
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        prescription = get_object_or_404(Prescription, id=pk)
        prescription.delete()

        return Response(status=204)



class PrescriptionItemListAPIView(APIView):
    def get(self, request):
        prescriptionitems = PrescriptionItem.objects.all()
        serializer = PrescriptionItemSerializer(prescriptionitems, many = True)

        return Response(serializer.data)

    def post(self, request):
        serializer = PrescriptionItemSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


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
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        prescriptionitem = get_object_or_404(PrescriptionItem, id=pk)
        prescriptionitem.delete()

        return Response(status=204)