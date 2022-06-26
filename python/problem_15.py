from tools import Benchmarked


@Benchmarked
def problem_15(grid_size=20):
    ret = 1
    for i in range(grid_size):
        ret = ret * ((2 * grid_size) - i) // (i + 1)
    return ret


if __name__ == "__main__":
    problem_15()
