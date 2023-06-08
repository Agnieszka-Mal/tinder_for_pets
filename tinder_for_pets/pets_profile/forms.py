import geocoder
from django import forms


from . import models
from .models import PetsImage, PetsProfile
from django.contrib.gis.geos import Point



# class PointWidget(forms.TextInput):
#     template_name = 'pets_profile/point_widget.html'  # Twój własny szablon HTML dla pola Point
#

# class PointField(forms.CharField):
#     widget = PointWidget
#
#     def to_python(self, value):
#         if isinstance(value, str):
#             try:
#                 location = geocoder.osm(value)
#                 if location.ok:
#                     longitude = location.json['lng']
#                     latitude = location.json['lat']
#                     return Point(float(longitude), float(latitude), srid=4326)
#             except (ValueError, TypeError):
#                 pass
#         return None


class PetsProfileForm(forms.ModelForm):
    #location = PointField()
    class Meta:
        model = models.PetsProfile
        fields = ('pets_name', 'type_of_pet', 'breed', 'sex', 'age', 'description', 'activity', 'profile_foto', 'city')
        widgets = {
            'profile_foto': forms.FileInput(attrs={'accept': 'image/*'}),
            #'location': forms.TextInput(attrs={'class': 'form-control'}),
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
        fields = ('pets_name', 'type_of_pet', 'breed', 'sex', 'age', 'description', 'activity', 'profile_foto', 'location')
        widgets = {
            'profile_foto': forms.FileInput(attrs={'accept': 'image/*'}),
        }