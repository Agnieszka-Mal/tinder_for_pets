from django import forms
from . import models

class ContactMessageForm(forms.ModelForm):

    """Form for creating a contact message."""
    class Meta:
        model = models.ContactMessage
        fields = ("name", "email", "message")