from audioop import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from . import models
from .forms import PetsProfileForm, PetsImageForm, PetsProfileEditForm
from .models import PetsProfile, PetsImage



class PetsProfileCreateView(LoginRequiredMixin, CreateView):
    model = PetsProfile
    form_class = PetsProfileForm
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        pets_profile = form.save(commit=False)
        pets_profile.users_id = self.request.user.id
        pets_profile.save()
        return super().form_valid(form)

class MyPetsProfilesDetailsView(LoginRequiredMixin, ListView):
    model = PetsProfile
    template_name = 'pets_profile/pets_profiles.html'
    context_object_name = 'pets_profiles'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        pets_profiles = PetsProfile.objects.filter(users=user)
        user_images = PetsImage.objects.filter(users=user)
        context['pets_profiles'] = pets_profiles
        context['user_images'] = user_images
        return context

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
    fields = ['pets_name', 'type_of_pet', 'breed', 'sex', 'age', 'description', 'activity', 'profile_foto']
    success_url = reverse_lazy('pets_profile:my_pets_profiles')

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        return queryset.filter(users=user)

class PetsProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = PetsProfile
    template_name = 'pets_profile/delete_profile.html'
    success_url = reverse_lazy('pets_profile:my_pets_profiles')

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        return queryset.filter(users=user)

    def form_valid(self, form):
        messages.success(self.request, 'Twój profil został pomyślnie usunięty. Proszę załóż profil, aby korzystać z aplikacji')
        return super().form_valid(form)

