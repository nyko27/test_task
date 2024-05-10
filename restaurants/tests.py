import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient

from .models import Restaurant


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def user(db):
    User = get_user_model()
    return User.objects.create_user(username='testuser', password='testpass', first_name='Test', last_name='User')


@pytest.fixture
def restaurant(db):
    return Restaurant.objects.create(name="Test Restaurant", address="Test Address", phone_number="1234567890")


# run tests from root directory using command -  'pytest restaurants/tests.py'

@pytest.mark.django_db
def test_restaurant_create_view(client, user):
    client.force_authenticate(user=user)
    url = reverse('create_restaurant')
    data = {'name': 'Test Restaurant', 'address': 'Test Address', 'phone_number': '1234567890'}
    response = client.post(url, data, format='json')
    assert response.status_code == 201


@pytest.mark.django_db
def test_restaurant_dishes_view(client, user, restaurant):
    client.force_authenticate(user=user)
    url = reverse('restaurant_dishes', kwargs={'restaurant_name': restaurant.name})
    response = client.get(url)
    assert response.status_code == 200
