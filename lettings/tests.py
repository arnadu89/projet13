import pytest
from django.test import Client
from django.urls import reverse
from lettings.models import Address, Letting


@pytest.mark.django_db
def test_letting_index():
    client = Client()

    url = reverse("lettings_index")
    response = client.get(url)

    title = "<title>Lettings</title>"
    content = response.content.decode()

    assert response.status_code == 200
    assert title in content


@pytest.mark.django_db
def test_letting_view():
    client = Client()

    address = Address.objects.create(
        number=1,
        street="Grande Rue",
        city="Orléans",
        state="Loiret",
        zip_code="45000",
        country_iso_code="45",
    )

    letting = Letting.objects.create(
        title="Some letting title",
        address=address
    )

    url = reverse("letting", kwargs={"letting_id": 1})
    response = client.get(url)

    title = f"<title>{letting.title}</title>"
    content = response.content.decode()

    assert response.status_code == 200
    assert title in content
