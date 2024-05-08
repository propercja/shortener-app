from typing import Dict

import pytest
from django.conf import settings

from shortener.serializers import LinkMapperSerializer


@pytest.fixture(autouse=True)
def override_settings() -> None:
    settings.ALPHABET = "abcdef"


@pytest.fixture
def valid_data() -> Dict[str, str]:
    return {"long_link": "https://example.com"}


@pytest.fixture
def invalid_data() -> Dict[str, str]:
    return {"long_link": ""}


@pytest.fixture
def serializer(valid_data: Dict[str, str]) -> LinkMapperSerializer:
    return LinkMapperSerializer(data=valid_data)
