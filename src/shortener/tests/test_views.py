import pytest
from django.urls import reverse
from rest_framework import status

from shortener.models import LinkMapper


@pytest.mark.django_db
class TestCreateShortlinkView:
    def test_create_shortlink(self, client) -> None:
        url = reverse("create-short-link")
        data = {"long_link": "https://example.com/very/long/url"}
        expected_short_link = "http://testserver/short/bbcde"

        response = client.post(url, data, format="json")

        assert response.status_code == status.HTTP_201_CREATED
        assert "short_link" in response.data
        assert response.data["short_link"] == expected_short_link
        assert LinkMapper.objects.filter(long_link=data["long_link"]).exists()


@pytest.mark.django_db
class TestRetrieveOrignalUrlView:
    def test_retrieve_original_url(self, client) -> None:
        link_mapper = LinkMapper.objects.create(
            long_link="https://example.com/very/long/url"
        )
        short_link = link_mapper.short_value
        url = reverse("retrieve-orig-link", kwargs={"short_link": short_link})

        response = client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["long_link"] == link_mapper.long_link

    def test_retrieve_original_url_invalid_shortlink(self, client) -> None:
        invalid_url = reverse(
            "retrieve-orig-link",
            kwargs={"short_link": "eeeeee"}
            )

        response = client.get(invalid_url)

        assert response.status_code == status.HTTP_404_NOT_FOUND
