from typing import Dict

import pytest
from rest_framework.reverse import reverse

from shortener.models import LinkMapper
from shortener.serializers import LinkMapperSerializer


@pytest.mark.django_db
class TestLinkMapperSerializer:

    def test_serializer_creates_instance(
        self, serializer: LinkMapperSerializer
    ) -> None:
        serializer.is_valid()
        instance = serializer.save()
        assert isinstance(instance, LinkMapper)

    @pytest.mark.parametrize(
        "input_data, serialized_data",
        [
            (
                {"long_link": "http://some_long.link", "id": 0},
                {
                    "long_link": "http://some_long.link",
                    "short_link": reverse(
                        "retrieve-orig-link", kwargs={"short_link": "abcde"}
                    ),
                },
            ),
            (
                {"long_link": "http://some_long.link", "id": 5},
                {
                    "long_link": "http://some_long.link",
                    "short_link": reverse(
                        "retrieve-orig-link", kwargs={"short_link": "fbcde"}
                    ),
                },
            ),
            (
                {"long_link": "http://some_long.link", "id": 5**5 - 1},
                {
                    "long_link": "http://some_long.link",
                    "short_link": reverse(
                        "retrieve-orig-link", kwargs={"short_link": "efefa"}
                    ),
                },
            ),
        ],
    )
    def test_link_mapper_serializer(
        self, input_data: Dict[str, str], serialized_data: Dict[str, str]
    ) -> None:

        mapper = LinkMapper(**input_data)
        serializer = LinkMapperSerializer(instance=mapper)
        assert serializer.data == serialized_data
