import pytest
from django.test import Client
from django.urls import reverse


def test_dummy():
    assert 1


@pytest.mark.django_db
def test_index():
    client = Client()

    url = reverse("index")
    response = client.get(url)

    title = "<title>Holiday Homes</title>"
    content = response.content.decode()

    assert response.status_code == 200
    assert title in content
