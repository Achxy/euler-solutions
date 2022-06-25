from math import factorial

from tools import Benchmarked


@Benchmarked
def problem_20(digit=100):
    return sum(map(int, str(factorial(digit))))


if __name__ == "__main__":
    problem_20()
