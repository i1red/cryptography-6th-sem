import os
from typing import Final, Callable

import pytest

from algorithms.primality_test import fermat_test, miller_rabin_test
from test.utils import is_prime_naive

SMALL_PRIMES: Final[set[int]] = {
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
    31, 37, 41, 43, 47, 53, 59, 61, 67,
    71, 73, 79, 83, 89, 97
}


@pytest.mark.parametrize('primality_test_function', [fermat_test, miller_rabin_test])
def test_primality_small_numbers(primality_test_function: Callable):
    for number in range(100):
        checks_count = 3 if number > 3 else 1
        if primality_test_function(number, checks_count):
            assert number in SMALL_PRIMES


@pytest.mark.parametrize('primality_test_function', [fermat_test, miller_rabin_test])
def test_primality_big_numbers(primality_test_function: Callable):
    probably_primes = [number for number in range(100_000, 300_000) if primality_test_function(number)]
    primes = [number for number in probably_primes if is_prime_naive(number)]

    assert len(primes) / len(probably_primes) > 0.99


if __name__ == '__main__':
    pytest.main([os.path.relpath(__file__), '-v'])
