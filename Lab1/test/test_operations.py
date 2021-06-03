import os
from itertools import product

import pytest

from algorithms.operations import bin_pow, karatsuba_mul
from algorithms.utils import randint_set


def test_bin_pow_small_numbers():
    for value, power, modulo in product(range(10), range(10), range(1, 10)):
        assert bin_pow(value, power, modulo) == value ** power % modulo


def test_bin_pow_big_numbers():
    for value, power, modulo in product(
            randint_set(1_000_000, 10_000_000, set_length=5),
            randint_set(1_000_000, 10_000_000, set_length=5),
            randint_set(1_000_000, 10_000_000, set_length=5)
    ):
        assert bin_pow(value, power, modulo) == pow(value, power, modulo)


def test_karatsuba_mul_small_numbers():
    for left_operand, right_operand in product(range(10), range(10)):
        assert karatsuba_mul(left_operand, right_operand) == left_operand * right_operand


def test_karatsuba_mul_big_numbers():
    for x, y in product(
            randint_set(1_000_000, 10_000_000, set_length=5),
            randint_set(1_000_000, 10_000_000, set_length=5),
    ):
        assert karatsuba_mul(x, y) == x * y


if __name__ == '__main__':
    pytest.main([os.path.relpath(__file__), '-v'])
