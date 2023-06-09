from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.views import View

from . import forms
class RegistrationView(View):

    """View class for user registration.

    This class handles the GET and POST requests for user registration.
    """
    def get(self, request):
        form = forms.RegistrationForm()
        return render(request, 'users/registration.html', {'form': form})


    def post(self,request):
        form = forms.RegistrationForm(request.POST or None)
        if form.is_valid():
            messages.add_message(request, messages.WARNING, f"Jesteś zarejestrowany. Proszę zaloguj się do aplikacji")
            form.save()

            return redirect(reverse('login'))

        return render(request, 'users/registration.html', {'form': form})

def login_user_view(request):

    """View function for user login.

    This function handles the login process for users.
    """

    if request.method == 'POST':
        form = forms.LoginForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.add_message(request, messages.SUCCESS, f'Jesteś zalogowany. Witaj {username}!')
                    return redirect(reverse('pets_profile:my-profiles-list'))
    else:
        form = forms.LoginForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):

    """View function for user logout.

    This function handles the logout process for users.
    """

    logout(request)
    return redirect(reverse('home:home'))
