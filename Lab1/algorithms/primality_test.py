from algorithms.utils import randint_set


def fermat_test(n: int, checks_count: int = 40) -> bool:
    if n < 2:
        return False

    return all(pow(a, (n - 1), n) == 1 for a in randint_set(1, n - 1, checks_count))


def miller_rabin_test(n: int, checks_count: int = 40) -> bool:
    if n < 2:
        return False

    if n % 2 == 0:
        return n == 2

    m, t = (n - 1) // 2, 1
    while m % 2 == 0:
        m, t = m // 2, t + 1

    for a in randint_set(1, n - 1, checks_count):
        u = pow(a, m, n)
        if u != 1:
            j = 0

            while u != n - 1 and j < t - 1:
                u = pow(u, 2, n)
                j += 1

            if u != n - 1:
                return False

    return True
