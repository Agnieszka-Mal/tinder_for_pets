from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views
from .views import PetsProfileCreateView, MyPetsProfilesDetailsView, PetsImageAddView, PetsProfileUpdateView, \
    PetsProfileDeleteView, MyPetsProfilesListView, AcceptProfileView

app_name = 'pets_profile'

urlpatterns = [
    path('create/', PetsProfileCreateView.as_view(), name='create-profile'),
    path('my-pets-profiles/<int:profile_id>/', login_required(MyPetsProfilesDetailsView.as_view()), name='my_pets_profiles'),
    path('accept-profile/<int:pk>/', AcceptProfileView.as_view(), name='accept-profile'),
    path('add-images/', PetsImageAddView.as_view(), name='add-images'),
    path('edit-profile/<int:pk>/', PetsProfileUpdateView.as_view(), name='edit_profile'),
    path('delete/<int:pk>/', PetsProfileDeleteView.as_view(), name='delete-profile'),
    path('my-profiles/', MyPetsProfilesListView.as_view(), name='my-profiles-list')
]
