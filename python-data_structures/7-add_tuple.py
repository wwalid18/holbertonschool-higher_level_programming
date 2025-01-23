#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """My addition function

    Args:
        tuple_a: first integer
        tuple_b: second integer

    Returns:
        The return value. tuple_a + tuple_b
    """
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    return (a[0] + b[0], a[1] + b[1])
