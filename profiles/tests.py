import pytest
from django.test import Client
from django.urls import reverse
from profiles.models import Profile
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_profile_index():
    client = Client()

    url = reverse("profiles_index")
    response = client.get(url)

    title = "<title>Profiles</title>"
    content = response.content.decode()

    assert response.status_code == 200
    assert title in content


@pytest.mark.django_db
def test_profile_view():
    client = Client()

    user = User.objects.create_user(
        "johnUsername",
        "john@doe.com",
        "johnPassword"
    )

    profile = Profile.objects.create(
        user=user,
        favorite_city="Orléans"
    )

    url = reverse("profile", kwargs={"username": user.username})
    response = client.get(url)

    title = f"<title>{ profile.user.username }</title>"
    content = response.content.decode()

    assert response.status_code == 200
    assert title in content
