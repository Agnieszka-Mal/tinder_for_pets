import django
from django.contrib.auth.models import User
from django.db import models

#rom users.models import TinderUser


class PetsProfile(models.Model):
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


    def __str__(self):
        return self.pets_name

class ItemBase(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('created_at',)
class PetsImage(ItemBase):
    photo = models.ImageField(upload_to='images')

