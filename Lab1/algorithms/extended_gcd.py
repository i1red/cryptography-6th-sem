from typing import NamedTuple


class ExtendedGCDResult(NamedTuple):
    gcd: int
    x: int
    y: int


def extended_gcd(left_operand: int, right_operand: int) -> ExtendedGCDResult:
    if left_operand == 0:
        return ExtendedGCDResult(right_operand, 0, 1)
    else:
        gcd, x, y = extended_gcd(right_operand % left_operand, left_operand)
        return ExtendedGCDResult(gcd, y - right_operand // left_operand * x, x)
