from benchmark import Benchmarked
from pathlib import Path

PATH = Path(__file__).parent.parent / "data" / "p013_numbers.txt"


@Benchmarked
def problem_13(data):
    return str(sum(data))[:10]


def _get_data(path):
    with open(path) as f:
        return map(int, f.read().splitlines())


if __name__ == "__main__":
    data = _get_data(PATH)
    problem_13(data)
