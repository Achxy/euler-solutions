from tools import Benchmarked


@Benchmarked
def problem_6(lim=100):
    return int(((lim * (lim + 1) // 2) ** 2) - (lim + 1) * lim / 6 * (2 * lim + 1))


if __name__ == "__main__":
    problem_6()
