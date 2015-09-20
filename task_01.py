#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Temperature conversion """

import decimal

decimal.getcontext().prec = 5

ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')


def fahrenheit_to_kelvin(degrees):
    """ Convert temperature from Farenheit to Kelvin units.

    Args:
        degrees (float): Farenheit temperature units to convert.

    Returns:
        Decimal: Temperature unit in Kelvin.

    Examples:
        >>> task_01.fahrenheit_to_kelvin(212)
        Decimal('373.15')
    """

    kelvin = celsius_to_kelvin(fahrenheit_to_celsius(degrees))
    return kelvin


def celsius_to_kelvin(degrees):
    """ Convert temperature from Celsius to Kelvin units.

    Args:
        degrees (float): Celsius units to convert.

    Returns:
        Decimal: Temperature unit in Kelvin.

    Examples:
        >>> task_01.celsius_to_kelvin(100)
        Decimal('373.15')
    """

    kelvin = decimal.Decimal(degrees) + ABSOLUTE_DIFFERENCE
    return kelvin


def fahrenheit_to_celsius(degrees):
    """ Convert temperature from Farenheit to Celsius units.

    Args:
        degrees (float): Farenheit value to convert to Celsius

    Returns:
        Decimal: Temperature unit in Celsius.
    Examples:
        >>> task_01.fahrenheit_to_celsius(212)
        Decimal('100')
    """

    celsius = decimal.Decimal(5) * \
        decimal.Decimal(float(degrees) - 32) / decimal.Decimal(9)
    return celsius
