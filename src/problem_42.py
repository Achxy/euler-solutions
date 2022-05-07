from __future__ import annotations

from functools import cache
from pathlib import Path

from benchmark import Benchmarked

PATH: Path = Path(__file__).parent.parent / "data" / "p042_words.txt"


@cache
def _is_triange_number(t) -> bool:
    # ∵ tn = n/2(n + 1)
    # => 0.5n^2 + 0.5n - tn = 0
    # d = √(b^2 - 4ac)

    # (in this case we have 2 real solutions)
    # ie, discriminant ∈ ℕ
    # We return if positive solution is natural
    di = (0.25 + (2 * t)) ** 0.5
    return not (0.5 - di) % 1


def _convert(data: list[str]) -> list[int]:
    # Precondition: constituent strings are all uppercase
    return [sum(ord(k) - 64 for k in d) for d in data]


def _parse(data: str) -> list[str]:
    return [d.strip().replace('"', "").upper() for d in data.split(",")]


def get_data(path=PATH) -> list[int]:
    with open(path, "r") as f:
        dt: str = f.read()
    return _convert(_parse(dt))


@Benchmarked
def problem_42(data=get_data()):
    return sum(1 for n in data if _is_triange_number(n))


if __name__ == "__main__":
    problem_42()
    print(f"Cache info of triangle number finder : {_is_triange_number.cache_info()}")
