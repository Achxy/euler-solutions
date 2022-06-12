from benchmark import Benchmarked
from pathlib import Path

PATH = Path(__file__).parent.parent / "data" / "p013_numbers.txt"


def _get_data(path=PATH):
    with open(path) as f:
        return map(int, f.read().splitlines())


@Benchmarked
def problem_13(data=_get_data()):
    return str(sum(data))[:10]


if __name__ == "__main__":
    problem_13()
