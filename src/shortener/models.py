"""
Module containing Django models for the shortener app.

This module defines the following models:
- LinkMapper: Represents a mapping between a long URL and a short URL.
"""

from django.db import models

from shortener.utils import int_to_short


class LinkMapper(models.Model):
    """
    Model storing long links  and mapps them to short links.
    """

    long_link = models.CharField(max_length=2048)

    @property
    def short_value(self) -> str:
        """
        Method returning the short value based on the object's identifier.

        Returns:
            str: Short value.
        """
        return int_to_short(self.id)
