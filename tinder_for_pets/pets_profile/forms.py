import geocoder
from django import forms
from . import models
from .models import PetsImage, PetsProfile

class PetsProfileForm(forms.ModelForm):

    """Form for creating or updating a pet's profile.

    This form handles the fields related to a pet's profile, including pet's name, type, breed, sex, age, description,
    activity, profile photo, and city."""
    class Meta:
        model = models.PetsProfile
        fields = ('pets_name', 'type_of_pet', 'breed', 'sex', 'age', 'description', 'activity', 'profile_foto', 'city')
        widgets = {
            'profile_foto': forms.FileInput(attrs={'accept': 'image/*'}),
        }



class PetsImageForm(forms.ModelForm):

    """Form for uploading pet images.

    This form handles the field related to uploading pet images."""

    class Meta:
        model = PetsImage
        fields = ('photo',)
        widgets = {
            'profile_foto': forms.FileInput(attrs={'accept': 'image/*'}),
        }



class PetsProfileEditForm(forms.ModelForm):

    """Form for editing a pet's profile."""
    class Meta:
        model = models.PetsProfile
        fields = ('pets_name', 'type_of_pet', 'breed', 'sex', 'age', 'description', 'activity', 'profile_foto', 'location')
        widgets = {
            'profile_foto': forms.FileInput(attrs={'accept': 'image/*'}),
        }