from typing import Final

import numpy as np


INT_BIT_SIZE: Final[int] = 32


def hex_pi_digit_generator():
    N = 0
    n, d = 0, 1
    while True:
        xn = (120 * N ** 2 + 151 * N + 47)
        xd = (512 * N ** 4 + 1024 * N ** 3 + 712 * N ** 2 + 194 * N + 15)
        n = ((16 * n * xd) + (xn * d)) % (d * xd)
        d *= xd
        yield 16 * n // d
        N += 1


# python doesnt have bitwise rotations and uses big integer (not int32), so I use this rotation algorithm
def int_rotate_left(integer: int, shift: int) -> int:
    s = np.binary_repr(integer, INT_BIT_SIZE).rjust(INT_BIT_SIZE, '0')
    return int(s[shift:] + s[:shift], 2)


def int_rotate_right(integer: int, shift: int) -> int:
    s = np.binary_repr(integer, INT_BIT_SIZE).rjust(INT_BIT_SIZE, '0')
    return int(s[INT_BIT_SIZE - shift:] + s[:INT_BIT_SIZE - shift], 2)
