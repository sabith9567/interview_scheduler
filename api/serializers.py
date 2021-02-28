from rest_framework import serializers
from api.models import TimeSlot


class RegisterTimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = '__all__'

    def validate(self, attrs):
        if attrs['start_time'] > attrs['end_time']:
            raise serializers.ValidationError({"end_time": "end_time must be greater than start time"})
        return attrs


class GetSlotSerializer(serializers.Serializer):
    candidate_id = serializers.UUIDField(required=True)
    interviewer_id = serializers.UUIDField(required=True)