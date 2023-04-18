from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from elevator.models import Elevator
from .serializers import ElevatorSerializer

from django.db.models import Q


class ElevatorView(APIView):
    serializer_class = ElevatorSerializer

    def get(self, request):
        """This returns all of the elevators in the db"""
        all_elevators = Elevator.objects.all()
        serialized_request = ElevatorSerializer(all_elevators, many=True)
        return Response(serialized_request.data, status=status.HTTP_200_OK)

    def post(self, request):
        """This allows the user to create a new elevator"""

        new_elevator = ElevatorSerializer(data=request.data)

        try:
            new_elevator.is_valid(raise_exception=True)
            new_elevator.save()
            return Response(new_elevator.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(
                e.__dict__ if e.__dict__ else str(e),
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
            )

    def patch(self, request):
        """This returns the filtered elevators based on floor
        that the user has requested to go to
        """

        requested_floor = request.data["requested_floor"]
        filtered_elevators = Elevator.objects.filter(
            Q(starting_floor__lte=requested_floor)
            & Q(ending_floor__gte=requested_floor)
        )
        serialized_request = ElevatorSerializer(filtered_elevators, many=True)
        return Response(serialized_request.data, status=status.HTTP_202_ACCEPTED)
