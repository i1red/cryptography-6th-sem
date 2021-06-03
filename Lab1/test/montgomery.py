import os
import random
from itertools import product

import pytest

from algorithms.montgomery import Montgomery
from algorithms.utils import randint_set


def test_montgomery_mul():
    modulo = random.randrange(1_000_001, 10_000_000, 2)
    montgomery = Montgomery(modulo)

    for a, b in product(randint_set(500_000, 10_000_000, set_length=5), randint_set(500_000, 10_000_000, set_length=5)):
        converted_a, converted_b = montgomery.convert_in(a), montgomery.convert_in(b)
        result = montgomery.convert_out(montgomery.mul(converted_a, converted_b))
        assert result == a * b % modulo


def test_montgomery_pow():
    modulo = random.randrange(1_000_001, 10_000_000, 2)
    montgomery = Montgomery(modulo)

    for value, power in product(randint_set(500_000, 10_000_000, set_length=5), randint_set(500_000, 10_000_000, set_length=5)):
        converted_value = montgomery.convert_in(value)
        result = montgomery.convert_out(montgomery.pow(converted_value, power))
        assert result == pow(value, power, modulo)


if __name__ == '__main__':
    pytest.main([os.path.relpath(__file__), '-v'])