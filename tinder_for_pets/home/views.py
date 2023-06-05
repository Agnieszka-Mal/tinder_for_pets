from audioop import reverse

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView

from . import forms

from django.urls import reverse
from django.contrib import messages

#from pets_profile.models import PetsProfile


# Create your views here.
def home(request):
    ctx = 'Hello, please login or register'
    return render(request, 'home/index.html', context={
        'ctx': ctx
    })

# class HomeView(TemplateView):
#     template_name = 'home/index.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         if self.request.user.is_authenticated:
#             user = self.request.user
#             pets_profile = PetsProfile.objects.filter(users=user).first()
#             context['pets_profile'] = pets_profile
#         return context



def contact(request):
    form = forms.ContactMessageForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Dziękujemy za wiadomość')
            return redirect(reverse('home:home'))


    return render(request, "home/contact.html", {"form": form})