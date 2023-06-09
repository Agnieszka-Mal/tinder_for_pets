
from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent='tinder_for_pets_app')

class PetsProfile(models.Model):

    """Model class representing a pet's profile.

    This class defines the fields and behavior of a pet's profile."""

    TYPE_OF_PET = (
        ('kot', 'kot'),
        ('pies', 'pies'),
    )

    SEX = (
        ('female', 'female'),
        ('male', 'male'),
    )

    ACTIVITY = (
        (1, 'spacery'),
        (2, 'bieganie'),
        (3, 'wędrówki'),
        (4, 'spotkania'),
        (5, 'sport'),
        (6, 'słodkie lenistwo'),
        (7, 'dobre jedzonko'),
    )

    users = models.ForeignKey(User, on_delete=models.CASCADE, db_column='users_id')
    pets_name = models.CharField(max_length=30, null=False, blank=False)
    type_of_pet = models.CharField(choices=TYPE_OF_PET, blank=False)
    breed = models.CharField(max_length=128)
    sex = models.CharField(choices=SEX)
    age = models.DecimalField(max_digits=3, decimal_places=1)
    description = models.TextField()
    activity = models.IntegerField(choices=ACTIVITY, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    profile_foto = models.ImageField(upload_to='pets_profile')
    location = models.PointField(null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=False)
    connected_profiles = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.pets_name



    def save(self, *args, **kwargs):

        """Overrides the save method to automatically set the location based on the city.

        If the location is not provided but the city is, the method uses geocoding to retrieve the
        coordinates (longitude and latitude) based on the city and sets the location field accordingly."""

        if not self.location and self.city:
            geolocator = Nominatim(user_agent="myapp")
            location = geolocator.geocode(self.city)
            if location:
                longitude = location.longitude
                latitude = location.latitude
                self.location = Point(float(longitude), float(latitude), srid=4326)
        super().save(*args, **kwargs)




class ItemBase(models.Model):

    """Abstract base model class for items.

    This class defines the common fields and behavior of items."""

    users = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('created_at',)
class PetsImage(ItemBase):

    """Model class for pet images.

    This class represents pet images and inherits from the `ItemBase` class."""

    photo = models.ImageField(upload_to='images')

