"""
Module containing Django REST Framework views for the shortener app.

This module defines the following views:
- CreateShortlinkView: View for creating short links.
- RetrieveOrignalUrlView: View for retrieving the original URL from
a short link.
"""

from typing import Any

from django.http import Http404
from rest_framework import generics

from shortener.models import LinkMapper
from shortener.serializers import LinkMapperSerializer
from shortener.utils import short_to_int


class CreateShortlinkView(generics.CreateAPIView):
    """
    API view for creating short links.
    """

    serializer_class = LinkMapperSerializer
    queryset = LinkMapper.objects.all()


class RetrieveOrignalUrlView(generics.RetrieveAPIView):
    """
    API view for retrieving the original URL from a short link.
    """

    queryset = LinkMapper.objects.all()
    serializer_class = LinkMapperSerializer

    def get_object(self) -> Any:
        """
        Get the LinkMapper object based on the provided short link.

        Raises:
            Http404: If the LinkMapper object does not exist for the provided
            short link.

        Returns:
            Any: The retrieved LinkMapper object.
        """
        shortener_pk = short_to_int(self.kwargs.get("short_link"))
        try:
            return self.queryset.get(pk=shortener_pk)
        except LinkMapper.DoesNotExist as exc:
            raise Http404 from exc
