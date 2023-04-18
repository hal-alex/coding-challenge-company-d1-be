import uuid

from django.db import models


class Elevator(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )

    starting_floor = models.IntegerField()
    ending_floor = models.IntegerField()

    elevator_name = models.CharField(max_length=250, blank=True)

    def save(self, *args, **kwargs):
        """Overriding default save db to generate the elevator name
        if it hasn't been provided in the request
        """
        if len(self.elevator_name) == 0:
            self.elevator_name = f"This elevator services floor {self.starting_floor} to floor {self.ending_floor}"
        super(Elevator, self).save(*args, **kwargs)
