"""Prime number utility functions."""

from __future__ import annotations


def is_prime(n: int) -> bool:
    """Return True if *n* is a prime number, False otherwise.

    This implementation uses the 6k ± 1 optimization to check for factors
    more efficiently after ruling out multiples of 2 and 3.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
