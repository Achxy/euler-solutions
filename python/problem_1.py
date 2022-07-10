from tools import Benchmarked
from numba import njit, uint16, uint8, uint32


@njit(uint32(uint16, uint8))
def _summation_of_progression(leng, num):
    k = leng // num
    return k * ((num + (num * k)) / 2)


@Benchmarked
def problem_1(length=1000):
    length -= 1
    return int(
        _summation_of_progression(length, 3)
        + _summation_of_progression(length, 5)
        - _summation_of_progression(length, 15)
    )


if __name__ == "__main__":
    problem_1()
