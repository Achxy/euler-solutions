from tools import Benchmarked


@Benchmarked
def problem_52():
    # all(set(str(n)) == x for x in map(lambda m: set(str(n * m)), range(2, 7)))
    return str((1 / 7))[2:8]


if __name__ == "__main__":
    problem_52()
