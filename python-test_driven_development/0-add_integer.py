#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two integers or floats and returns their sum.

    The function checks if both `a` and `b` are either integers or floats. 
    It raises a TypeError if either `a` or `b` is not an integer or float.

    Parameters:
    - a: The first number (integer or float).
    - b: The second number (integer or float). Defaults to 98 if not provided.

    Returns:
    - The sum of `a` and `b` as an integer, rounding any floats to the nearest integer.

    Raises:
    - TypeError: If either `a` or `b` is not an integer or a float.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
