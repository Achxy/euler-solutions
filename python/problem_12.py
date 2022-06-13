from collections import Counter
from itertools import count
from math import prod

from benchmark import Benchmarked


def factors(n: int) -> int:
    factors = Counter()
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factors[i] += 1
            n //= i
    if n > 1:
        factors[n] += 1
    return prod((factors + Counter(factors.keys())).values())


def tri(n: int) -> int:
    return n * (n + 1) >> 1


@Benchmarked
def problem_12(fac=500):
    for n in count(1):
        n_twice = 2 * n
        x = factors(n_twice + 1)
        if factors(n) * x >= fac:
            return tri(n_twice)
        if factors(n + 1) * x >= fac:
            return tri(n_twice + 1)
    raise ValueError("No solution found")


if __name__ == "__main__":
    problem_12()
