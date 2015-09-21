#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Farenheit to Celcius conversions"""

import decimal

ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')


def fahrenheit_to_celcius(degrees):
    """ Converts farenheit to Celcius

    Args:
        degrees (decimal): Degrees in Fahrenheit

    Returns:
        Returns temperature, converted in decmial form.

    Examples:

        >>> fahrenheit_to_celsius(212)
        Decimal('100')
    """
    degrees = (degrees - 32) * 5.0 / 9
    degrees = decimal.Decimal(degrees)
    return degrees


def celcius_to_kelvin(degrees):
    """Converts Celcius to Kelivn.

    Args:
        degrees (decimal): Degrees in Celcius

    Returns:
        Returns temperature, converted into decimal form.

    Examples:

        >>> celsius_to_kelvin(100)
        Decimal('373.15')
    """
    degrees = degrees + ABSOLUTE_DIFFERENCE
    degrees = decimal.Decimal(degrees)
    return degrees


def fahrenheit_to_kelvin(degrees):
    """Converts Fahrenheit to Kelvin.

    Args:
        degrees (decimal): Degrees in Farenheit

    Returns:
        Returns temperature, converted from Farenheit to Kelvin, decimal form.

    Examples:

        >>> fahrenheit_to_kelvin(212)
        Decimal('373.15')
    """
    degrees = celcius_to_kelvin(fahrenheit_to_celcius(degrees))
    degrees = decimal.Decimal(degrees)
    return degrees
