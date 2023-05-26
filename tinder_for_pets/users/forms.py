from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError

from . import models

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'placeholder': 'Min.8 characters, digits, and special characters.',
        'class': 'magic-input'
    }))

    password_confirmation = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    error_messages = {
        'email': {
            "unique": "Spróbuj użyć innego adresu Email"
        }
    }

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'first_name', 'password')

    def clean_password_confirmation(self):
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')

        if password and password_confirmation and password != password_confirmation:
            raise ValidationError('Hasła nie są takie same, spróbuj jeszcze raz')

        return password_confirmation

    def clean_username(self):
        username = self.cleaned_data.get("username")

        if username and len(username) < 3:
            raise ValidationError("Nazwa użytkownika jest za krótka!")

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError(self.error_messages['email']['unique'], code='unique')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        user.is_active = True

        if commit:
            user.save()

        return user

class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        label='Email',
        required=False,
        widget=forms.TextInput(attrs={
            'name': 'username',
            'placeholder': 'Email',

        })
    )

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        fields = ('username', 'password')

    error_messages = {
        "invalid_login": "Email i hasło nie pasują do żadnego użytkownika."
    }