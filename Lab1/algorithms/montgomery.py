from algorithms.extended_gcd import extended_gcd


class Montgomery:
    def __init__(self, modulo: int) -> None:
        if modulo < 3 or modulo % 2 == 0:
            raise ValueError("Modulus must be an odd number greater or equals 3")

        self.modulo = modulo

        self.bit_reducer = (modulo.bit_length() // 8 + 1) * 8
        self.reducer = 1 << self.bit_reducer

        gcd, x, _ = extended_gcd(self.reducer % modulo, modulo)
        if gcd != 1:
            raise ValueError('Reciprocal does not exist')

        self.reciprocal = x % modulo

    def convert_in(self, x):
        return (x << self.bit_reducer) % self.modulo

    def convert_out(self, x):
        return (x * self.reciprocal) % self.modulo

    def mul(self, left_operand: int, right_operand: int) -> int:
        product = left_operand * right_operand

        temp = ((product & (self.reducer - 1)) * ((self.reducer * self.reciprocal - 1) // self.modulo)) & (self.reducer - 1)
        reduced = (product + temp * self.modulo) >> self.bit_reducer

        return reduced if reduced < self.modulo else reduced - self.modulo

    def pow(self, value: int, power: int) -> int:
        result = self.reducer % self.modulo

        while power != 0:
            if (power & 1) == 1:
                result = self.mul(result, value)
            value = self.mul(value, value)
            power >>= 1

        return result
