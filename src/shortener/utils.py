"""
Module for utility functions
"""

from django.conf import settings

ALPHABET = getattr(settings, "ALPHABET")


def int_to_short(number: int) -> str:
    """
    Converts an integer into a string value based on the specified ALPHABET.

    Args:
        number (int): The integer to convert.

    Returns:
        str: The string value representation.
    """
    base = len(ALPHABET)

    result = []
    pos = 0
    while number > 0:
        number, remainder = divmod(number, base)
        result.append(ALPHABET[(remainder + pos) % base])
        pos += 1

    while len(result) < 5:
        result.append(ALPHABET[len(result)])

    return "".join(result)


def short_to_int(short: str) -> int:
    """
    Converts a string value back into an integer based on the specified
    ALPHABET.

    Args:
        short (str): The string value representation.

    Returns:
        int: The integer.
    """
    base = len(ALPHABET)

    unmixed = [
        ((ALPHABET.index(val) - pos) % base) * base**pos
        for pos, val in enumerate(short)
    ]

    return sum(unmixed)
