from audioop import reverse
from django.shortcuts import render, redirect
from . import forms
from django.urls import reverse
from django.contrib import messages




def home(request):

    """View function for the home page."""

    ctx = 'Hello, please login or register'
    return render(request, 'home/index.html', context={
        'ctx': ctx
    })

#
def contact(request):

    """View function for handling the contact form."""

    form = forms.ContactMessageForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Dziękujemy za wiadomość')
            return redirect(reverse('home:home'))


    return render(request, "home/contact.html", {"form": form})