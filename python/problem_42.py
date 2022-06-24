from __future__ import annotations

from functools import cache

from benchmark import Benchmarked
from tools.helper import form_path


@cache
def _is_triange_number(t) -> bool:
    """
    ∵ tn = ½n(n+1)
    => tn = ([n^2] / 2 + n/2)
    Subtracting all sides by ([n^2] / 2 + n/2)
    tn - ([n^2] / 2 + n/2) = ([n^2] / 2 + n/2) - ([n^2] / 2 + n/2)
    so, tn - ([n^2] / 2 + n/2) = 0
    ∴ - 0.5n^2 - 0.5n + tn = 0

    Hence, d = (0.25 + (2 * t)) ** 0.5
    since, d > 0 we say can say we have distinct bifurcate numbers
    The positive solution is deemed triangular if it is natural
    ie, da ∈ N
    """
    return not (0.5 - ((0.25 + (2 * t)) ** 0.5)) % 1


def _convert(data: list[str]) -> list[int]:
    # Precondition: constituent strings are all uppercase
    return [sum(ord(k) - 64 for k in d) for d in data]


def _parse(data: str) -> list[str]:
    # Another way is to `literal_eval("[" + data + "]")`
    return [d.strip().replace('"', "").upper() for d in data.split(",")]


def get_data(path=form_path("p042_words.txt")) -> list[int]:
    with open(path, "r") as f:
        dt: str = f.read()
    return _convert(_parse(dt))


@Benchmarked
def problem_42(data=get_data()):
    return sum(_is_triange_number(n) for n in data)


if __name__ == "__main__":
    problem_42()
    print(f"Cache info of triangle number finder : {_is_triange_number.cache_info()}")
