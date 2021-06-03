import os
import zlib

import pytest

from adler32 import adler32
from utils import random_bytes


def test_alder32():
    for alder in range(10):
        for _ in range(10):
            char_sequence = random_bytes()
            assert adler32(char_sequence, alder) == zlib.adler32(char_sequence, alder)


if __name__ == '__main__':
    pytest.main([os.path.relpath(__file__), '-v'])
