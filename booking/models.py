from django.db import models
from django.conf import settings
from django.urls import reverse_lazy


class Room_Categories(models.Model):
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=1000)


class Room(models.Model):
    number = models.IntegerField()
    category = models.ForeignKey(Room_Categories, on_delete=models.CASCADE)
    beds = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f'{self.number}. {self.category.name} with {self.beds}\
        beds for {self.capacity} people'


class Booking(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f'{self.user} booked {self.room} from {self.check_in}\
        to {self.check_out}'

    def get_cancel_booking_url(self):
        return reverse_lazy('booking:CancelBookingView', args=[self.pk, ])

    def get_room_category(self):
        return f'{self.room.category.name}'
