"""
Module containing Django REST Framework serializers for the shortener app.

This module defines serializers for the following models:
- LinkMapperSerializer: Serializes LinkMapper model instances
for use in API endpoints.
"""

from typing import Any, Dict

from rest_framework import serializers
from rest_framework.reverse import reverse

from shortener.models import LinkMapper


class LinkMapperSerializer(serializers.Serializer):
    """
    Serializer for the LinkMapper model.
    """

    long_link = serializers.CharField(max_length=2048)
    short_link = serializers.SerializerMethodField()

    class Meta:
        model = LinkMapper
        fields = ["long_link", "short_link"]

    def create(self, validated_data: Dict[str, Any]) -> LinkMapper:
        """
        Create and return a new LinkMapper instance, given the validated data.

        Args:
            validated_data (dict): The validated data to create the LinkMapper
            instance.

        Returns:
            LinkMapper: The created LinkMapper instance.
        """
        return LinkMapper.objects.create(**validated_data)

    def get_short_link(self, obj: LinkMapper) -> str:
        """
        Get the short link for the provided LinkMapper instance.

        Args:
            obj (LinkMapper): The LinkMapper instance.

        Returns:
            str: The short link.
        """
        request = self.context.get("request")
        return reverse(
            "retrieve-orig-link",
            kwargs={"short_link": obj.short_value},
            request=request,
        )
