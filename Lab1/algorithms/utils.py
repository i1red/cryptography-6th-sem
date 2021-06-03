import random


def randint_set(a: int, b: int, set_length: int) -> set[int]:
    if b - a + 1 < set_length:
        raise ValueError(f'Given set_length {set_length} is greater than maximum possible {b - a + 1}')

    result = set()
    while len(result) != set_length:
        result.add(random.randint(a, b))

    return result
