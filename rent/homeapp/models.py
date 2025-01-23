from django.db import models
import uuid
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Userprofile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    role=models.TextField()
    pincode=models.TextField()
    address=models.CharField(max_length=255)

class cardetails(models.Model):
    rent_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    carname = models.TextField(null=False)
    brand = models.TextField(null=False)
    year = models.IntegerField(null=True)
    price = models.IntegerField(null=False)
    fueltype = models.TextField()
    transmissiontype = models.TextField()
    image = models.ImageField(upload_to='car_images', null=True, blank=True)
    dealer = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  
    rental_status = models.CharField(
        max_length=20,
        default="Not Rented",
        choices=[("Not Rented", "Not Rented"), ("Rented", "Rented")]
    )
class bikedetails(models.Model):
    rent_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    bikename = models.TextField(null=False)
    brand = models.TextField(null=False)
    year = models.IntegerField(null=True)
    price = models.IntegerField(null=False)
    fueltype = models.TextField()
    image = models.ImageField(upload_to='bike_images', null=True, blank=True)
    dealer = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    rental_status = models.CharField(
        max_length=20,
        default="Not Rented",
        choices=[("Not Rented", "Not Rented"), ("Rented", "Rented")]
    )

class rentedcars(models.Model):
      rent_id= models.ForeignKey(cardetails, on_delete=models.CASCADE, related_name='rentals')
      rent_hours = models.PositiveIntegerField()
      rent_date = models.DateTimeField(auto_now_add=True)
      id_proof = models.ImageField(upload_to='id_proofs/', null=False, blank=False)
      user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
      @property
      def calculate_amount(self):
          return self.rent_hours * self.rent_id.price  
class rentedbikes(models.Model):
      rent_id= models.ForeignKey(bikedetails, on_delete=models.CASCADE, related_name='rentals')
      rent_hours = models.PositiveIntegerField()
      rent_date = models.DateTimeField(auto_now_add=True)
      id_proof = models.ImageField(upload_to='id_proofs/', null=False, blank=False)
      user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

