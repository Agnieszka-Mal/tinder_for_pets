import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import RequestFactory

from tinder_for_pets.pets_profile.forms import PetsProfileForm
from tinder_for_pets.pets_profile.models import PetsProfile
from tinder_for_pets.pets_profile.views import PetsProfileCreateView


@pytest.mark.django_db
def test_form_valid():
    user = User.objects.create_user(username='testuser', password='testpassword')

    form_data = {
        'pet_name': 'Fido',
        'type_of_pet': 'pies',
        'age': 3,
        'breed': 'pudel',
        'sex': 'male',
        'description': 'wariat',
        'activity': 1,
        'city': 'kraków',
    }
    form = PetsProfileForm(data=form_data)

    view = PetsProfileCreateView()
    view.request = RequestFactory().post(reverse('pets_profile:create'))
    view.request.user = user

    assert view.form_valid(form)

    assert PetsProfile.objects.count() == 1

    profile = PetsProfile.objects.first()
    assert profile.users_id == user.id

    assert view.get_success_url() == reverse('pets_profile:my-profiles-list')