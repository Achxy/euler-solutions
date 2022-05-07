from benchmark import Benchmarked
from math import factorial


@Benchmarked
def problem_20(digit=100):
    return sum(map(int, str(factorial(digit))))


if __name__ == "__main__":
    print(problem_20())
