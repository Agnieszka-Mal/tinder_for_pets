
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from .forms import PetsProfileForm, PetsImageForm
from .models import PetsProfile, PetsImage
from django.contrib.gis.db.models.functions import Distance



class PetsProfileCreateView(LoginRequiredMixin, CreateView):

    """View class for creating a pet's profile.

    This class handles the creation of a new pet's profile."""

    model = PetsProfile
    form_class = PetsProfileForm
    success_url = reverse_lazy('pets_profile:my-profiles-list')

    def form_valid(self, form):
        pets_profile = form.save(commit=False)
        pets_profile.users_id = self.request.user.id
        pets_profile.save()
        return super().form_valid(form)

class MyPetsProfilesDetailsView(LoginRequiredMixin, DetailView):

    """View class for displaying details of a pet's profile.

    This class handles the display of details for a specific pet's profile."""

    model = PetsProfile
    template_name = 'pets_profile/pets_profiles.html'
    context_object_name = 'selected_profile'

    def get_object(self, queryset=None):
        user = self.request.user
        profile_id = self.kwargs.get('profile_id')
        pets_profile = get_object_or_404(PetsProfile, id=profile_id, users=user)
        return pets_profile

    def get_context_data(self, **kwargs):

        """Adds additional context data to be used in the template rendering."""

        context = super().get_context_data(**kwargs)
        user_profile = self.get_object()
        nearby_profiles = PetsProfile.objects.exclude(users=self.request.user).annotate(
            distance=Distance('location', user_profile.location)).filter(distance__lte=100000)
        context['nearby_profiles'] = nearby_profiles
        accepted_profiles = PetsProfile.objects.filter(connected_profiles=user_profile)
        context['accepted_profiles'] = accepted_profiles
        return context




class AcceptProfileView(View):

    """View class for accepting or rejecting a pet's profile.

    This class handles the acceptance or rejection of a pet's profile."""

    def get(self, request, pk):
        profile = PetsProfile.objects.get(pk=pk)
        return render(request, 'pets_profile/accept_profile.html', {'profile': profile})

    def post(self, request, pk):
        profile = PetsProfile.objects.get(pk=pk)
        user_profile = self.request.user.petsprofile_set.first()
        action = request.POST.get('action')

        if action == 'accept':
            user_profile.connected_profiles.add(profile)
        elif action == 'reject':
            user_profile.connected_profiles.remove(profile)

        return redirect('pets_profile:my_pets_profiles', profile_id=user_profile.id)

class MyPetsProfilesListView(LoginRequiredMixin, ListView):

    """View class for displaying a list of user's pet profiles.

    This class handles the display of a list of pet profiles associated with the current user."""

    model = PetsProfile
    template_name = 'pets_profile/user_profiles.html'
    context_object_name = 'user_profiles'

    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset().filter(users=user)
        return queryset

class PetsImageAddView(LoginRequiredMixin, CreateView):

    """View class for adding pet images.

    This class handles the addition of pet images."""

    model = PetsImage
    form_class = PetsImageForm
    success_url = reverse_lazy('pets_profile:my_pets_profiles')

    def form_valid(self, form):
        form.instance.users = self.request.user
        return super().form_valid(form)



class PetsProfileUpdateView(LoginRequiredMixin, UpdateView):

    """View class for updating a pet's profile.

    This class handles the updating of a pet's profile."""

    model = PetsProfile
    template_name = 'pets_profile/edit_profile.html'
    fields = ['pets_name', 'type_of_pet', 'breed', 'sex', 'age', 'description', 'activity', 'profile_foto', 'city']

    def get_success_url(self):
        return reverse_lazy('pets_profile:my_pets_profiles', kwargs={'profile_id': self.object.pk})

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        return queryset.filter(users=user)

class PetsProfileDeleteView(LoginRequiredMixin, DeleteView):

    """View class for deleting a pet's profile.

    This class handles the deletion of a pet's profile."""

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

