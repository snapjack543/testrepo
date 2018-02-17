from django.db import models




# Create your models here.
class Reservations(models.Models):
    reservation_id = models.CharField(max_length=30, primary_key=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    request_time = models.DateTimeField(auto_now_add=True)



class Reservation_Actions(models.Models):
    reservation_id = models.ForeignKey('Reservations.reservation_id')
    #action = 
    
