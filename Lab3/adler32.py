from typing import Final


ADLER_MOD: Final[int] = 65521


def adler32(char_sequence: bytes, adler: int = 1) -> int:
    sum_ = 0

    for char in char_sequence:
        adler = (adler + char) % ADLER_MOD
        sum_ = (adler + sum_) % ADLER_MOD

    return adler | (sum_ << 16)
