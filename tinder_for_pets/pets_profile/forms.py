from django import forms
from . import models
from .models import PetsImage


class PetsProfileForm(forms.ModelForm):
    class Meta:
        model = models.PetsProfile
        fields = ('pets_name', 'type_of_pet', 'breed', 'sex', 'age', 'description', 'activity', 'profile_foto')
        widgets = {
            'profile_foto': forms.FileInput(attrs={'accept': 'image/*'}),
        }

class PetsImageForm(forms.ModelForm):
    class Meta:
        model = PetsImage
        fields = ('photo',)
        widgets = {
            'profile_foto': forms.FileInput(attrs={'accept': 'image/*'}),
        }



class PetsProfileEditForm(forms.ModelForm):
    class Meta:
        model = models.PetsProfile
        fields = ('pets_name', 'type_of_pet', 'breed', 'sex', 'age', 'description', 'activity', 'profile_foto')
        widgets = {
            'profile_foto': forms.FileInput(attrs={'accept': 'image/*'}),
        }