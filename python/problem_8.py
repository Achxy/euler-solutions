from math import prod

from tools import Benchmarked, form_path


def _get_data(path=form_path("p008_numbers.txt")):
    with open(path, "r") as f:
        return f.read().replace("\n", "")


@Benchmarked
def problem_8(data=_get_data(), adjacent=13):
    length = len(data)
    largest = 0
    for i in range(length - length % adjacent):
        product = prod(map(int, data[i : i + adjacent]))
        largest = product if product > largest else largest
    return largest


if __name__ == "__main__":
    problem_8()
