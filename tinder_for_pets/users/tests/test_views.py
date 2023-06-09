import pytest


from django.urls import reverse

def test_login_page(client):
    url = reverse('users:login')
    response = client.get(url)
    assert response.status_code == 200
    assert '<h1>Zaloguj się do aplikacji</h1>' in response.content.decode('UTF-8')



