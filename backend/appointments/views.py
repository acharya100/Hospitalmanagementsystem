from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from appointments.models import Appointment
from appointments.serializers import AppointmentSerializer
# Create your views here.

class AppointmentListAPIView(APIView):
    def get(self, request):
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many = True)

        return Response(serializer.data)

    def post(self, request):
        serializer = AppointmentSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class AppointmentDetailAPIView(APIView):
    def get(self, request, pk):
        appointment = get_object_or_404(Appointment, id=pk)
        serializer = AppointmentSerializer(appointment)

        return Response(serializer.data)

    def put(self, request,pk):
        appointment = get_object_or_404(Appointment, id=pk)
        serializer = AppointmentSerializer(appointment, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        appointment = get_object_or_404(Appointment, id=pk)
        appointment.delete()

        return Response(status=204)