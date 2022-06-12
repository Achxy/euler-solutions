from benchmark import Benchmarked
from helper import form_path


def _get_data(path=form_path("p013_numbers.txt")):
    with open(path) as f:
        return map(int, f.read().splitlines())


@Benchmarked
def problem_13(data=_get_data()):
    return str(sum(data))[:10]


if __name__ == "__main__":
    problem_13()
