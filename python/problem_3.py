from benchmark import Benchmarked


@Benchmarked
def problem_3(of=6_00_85_14_75_143):
    x = 2
    while x**2 < of:
        while of % x == 0:
            of //= x
        x += 1
    return of


if __name__ == "__main__":
    problem_3()
