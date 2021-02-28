import datetime

from django.shortcuts import render
from utils.helper import get_time_slots, get_time_slot_by_date, get_time_range_by_date
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status

from api.models import *
from api.serializers import *


class RegisterTimeSlot(CreateAPIView):
    serializer_class = RegisterTimeSlotSerializer


class GetTimeSlots(APIView):

    def post(self, request):
        serializer = GetSlotSerializer(data=request.data)
        if serializer.is_valid():
            if CustomUser.objects.filter(id=serializer.data.get('candidate_id')).exists() and CustomUser.objects.filter(id=serializer.data.get('interviewer_id')).exists:

                candidate_time_slot = TimeSlot.objects.values('start_time', 'end_time', 'available_date').\
                    filter(user__id=serializer.data.get('candidate_id')).order_by('-available_date')

                interviewer_time_slot = TimeSlot.objects.filter(user__id=serializer.data.get('interviewer_id'))\
                    .order_by('-available_date')

                interviewer_time_slot_by_date = get_time_range_by_date(interviewer_time_slot)
                candidate_time_slot_by_date = get_time_range_by_date(candidate_time_slot)

                available_slots_by_date = {}
                for date, slots in interviewer_time_slot_by_date.items():
                    available_slots = []
                    if candidate_time_slot_by_date.get(date):
                        for time_range_1 in slots:
                            for time_range_2 in candidate_time_slot_by_date.get(date):
                                try:
                                    if time_range_1.is_intersection(time_range_2):
                                        available_slots.append(time_range_1.intersection(time_range_2))
                                except Exception as e:
                                    return Response(data={
                                        'message': str(e)+' please use api for registering time slots , this is beacuse '
                                                          'your entry through admin for the candidate or interviewer '
                                                          'has end_time < start_time'}, status=status.HTTP_400_BAD_REQUEST)

                    available_slots_by_date[date] = available_slots

                data = get_time_slot_by_date(available_slots_by_date)
                if not data:
                    return Response(data={'message': "No available slots"}, status=status.HTTP_200_OK)
                return Response(data=data, status=status.HTTP_200_OK)

            else:
                return Response(data={'message': ' invalid candidate_id or interviewer_id'},
                                status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
