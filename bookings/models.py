from django.db import models

# Create your models here.
class Resources(models.Model):
    room_name = models.CharField(max_length=56, help_text="this is the room name", primary_key=True)
    available = models.BooleanField()

class BookingStatuses(models.Model):
    status = models.CharField(max_length=20, help_text="booking status")

class BookingAuditTrail(models.Model):

    booking = models.ForeignKey('Bookings', on_delete=models.CASCADE)
    status = models.ForeignKey('BookingStatuses', on_delete=models.CASCADE)
    creation_time =  models.DateTimeField('status time', auto_now_add=True)
    
class Bookings(models.Model):
    room_name = models.ForeignKey('Resources', on_delete=models.CASCADE)
    number_of_people =  models.IntegerField("Number of people for booking")
    start_time = models.DateTimeField('start time')    
    end_time = models.DateTimeField('end time')
    creation_time =  models.DateTimeField('booking request time',
                                          auto_now_add=True)
    
    

