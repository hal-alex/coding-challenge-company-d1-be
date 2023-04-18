from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from elevator.models import Elevator
from .serializers import ElevatorSerializer


class ElevatorView(APIView):
    serializer_class = ElevatorSerializer

    def get(self, request):
        """This returns all of the elevators in the db"""
        all_elevators = Elevator.objects.all()
        serialized_request = ElevatorSerializer(all_elevators, many=True)
        return Response(serialized_request.data, status=status.HTTP_200_OK)

    def post(self, request):
        """This allows us to create a new elevator"""

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
