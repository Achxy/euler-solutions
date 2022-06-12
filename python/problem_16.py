from benchmark import Benchmarked


@Benchmarked
def problem_16(power=1000):
    return sum(map(int, str(2**power)))


if __name__ == "__main__":
    problem_16()
