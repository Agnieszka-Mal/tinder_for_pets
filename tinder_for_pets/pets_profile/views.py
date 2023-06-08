from audioop import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from . import models
from .forms import PetsProfileForm, PetsImageForm, PetsProfileEditForm
from .models import PetsProfile, PetsImage
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from django.contrib.gis.db.models.functions import Distance



class PetsProfileCreateView(LoginRequiredMixin, CreateView):
    model = PetsProfile
    form_class = PetsProfileForm
    success_url = reverse_lazy('pets_profile:my-profiles-list')

    def form_valid(self, form):
        pets_profile = form.save(commit=False)
        pets_profile.users_id = self.request.user.id
        pets_profile.save()
        return super().form_valid(form)

class MyPetsProfilesDetailsView(LoginRequiredMixin, DetailView):
    model = PetsProfile
    template_name = 'pets_profile/pets_profiles.html'
    context_object_name = 'selected_profile'

    def get_object(self, queryset=None):
        user = self.request.user
        profile_id = self.kwargs.get('profile_id')
        pets_profile = get_object_or_404(PetsProfile, id=profile_id, users=user)
        return pets_profile

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            user_profile = self.get_object()
            nearby_profiles = PetsProfile.objects.exclude(users=self.request.user).annotate(
                distance=Distance('location', user_profile.location)).filter(distance__lte=100000)
            context['nearby_profiles'] = nearby_profiles
            accepted_profiles = PetsProfile.objects.filter(connected_profiles=user_profile)
            context['accepted_profiles'] = accepted_profiles
            return context

    def accept_profile(self, request, pk):
        user_profile = self.get_object()
        accepted_profile = PetsProfile.objects.get(pk=pk)
        user_profile.accept_profile(accepted_profile)
        return redirect('pets_profile:profile-details', profile_id=user_profile.id)


class MyPetsProfilesListView(LoginRequiredMixin, ListView):
    model = PetsProfile
    template_name = 'pets_profile/user_profiles.html'
    context_object_name = 'user_profiles'

    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset().filter(users=user)
        return queryset

class PetsImageAddView(LoginRequiredMixin, CreateView):
    model = PetsImage
    form_class = PetsImageForm
    success_url = reverse_lazy('pets_profile:my_pets_profiles')

    def form_valid(self, form):
        form.instance.users = self.request.user
        return super().form_valid(form)


class PetsProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = PetsProfile
    template_name = 'pets_profile/edit_profile.html'
    fields = ['pets_name', 'type_of_pet', 'breed', 'sex', 'age', 'description', 'activity', 'profile_foto', 'city']
    success_url = reverse_lazy('pets_profile:my_pets_profiles')

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        return queryset.filter(users=user)

class PetsProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = PetsProfile
    template_name = 'pets_profile/delete_profile.html'
    success_url = reverse_lazy('pets_profile:my-profiles-list')

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        return queryset.filter(users=user)

    def form_valid(self, form):
        messages.success(self.request, 'Twój profil został pomyślnie usunięty. Proszę załóż profil, aby korzystać z aplikacji')
        return super().form_valid(form)

