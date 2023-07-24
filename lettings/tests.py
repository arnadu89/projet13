import pytest
from pytest_mock import mocker
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_letting_index():
    client = Client()

    url = reverse("lettings_index")
    response = client.get(url)

    assert response.status_code == 200


# @pytest.mark.django_db
# def test_letting(mocker):
#     client = Client()
#
#     # mocked_letting = ""
#     #
#     # mocker.patch("", return_value=mocked_letting)
#
#     url = reverse("letting", kwargs={"letting_id": "1"})
#     response = client.get(url)
#
#     assert response.status_code == 200
