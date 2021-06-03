def is_prime_naive(number: int) -> int:
    square_root = int(number ** 0.5)

    for divisor in range(2, square_root + 1):
        if number % divisor == 0:
            return False

    return True
