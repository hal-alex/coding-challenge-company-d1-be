from rest_framework import serializers

from elevator.models import Elevator


class ElevatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elevator
        fields = ["id", "starting_floor", "ending_floor", "elevator_name"]
