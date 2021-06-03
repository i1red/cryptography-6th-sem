def bin_pow(value: int, power: int, modulo: int) -> int:
    if modulo == 1:
        return 0

    result = 1

    while power != 0:
        if (power & 1) == 1:
            result = result * value % modulo
        value = value * value % modulo
        power >>= 1

    return result


def karatsuba_mul(left_operand: int, right_operand: int) -> int:
    length = max(left_operand.bit_length(), right_operand.bit_length())
    if length < 2:
        return left_operand * right_operand

    shift = length // 2
    x = 1 << shift

    a, b, c, d = left_operand >> shift, left_operand & (x - 1), right_operand >> shift, right_operand & (x - 1)

    ac, bd = karatsuba_mul(a, c), karatsuba_mul(b, d)
    x_coef = karatsuba_mul(a + b, c + d) - (ac + bd)
    return (ac << 2 * shift) + (x_coef << shift) + bd
