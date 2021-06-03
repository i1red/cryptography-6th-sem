import os

import pytest

from algorithms.extended_gcd import extended_gcd
from algorithms.utils import randint_set


def test_extended_gcd():
    iterations_num = 1000
    for a, b in zip(randint_set(0, 100_000, iterations_num), randint_set(0, 100_000, iterations_num)):
        gcd, x, y = extended_gcd(a, b)

        for divisor in range(gcd + 1, int(min(a ** 0.5, b ** 0.5)) + 1):
            assert a % divisor != 0 or b % divisor != 0

        assert a * x + b * y == gcd


if __name__ == '__main__':
    pytest.main([os.path.relpath(__file__), '-v'])