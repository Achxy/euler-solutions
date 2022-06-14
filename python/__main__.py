from __future__ import annotations

import importlib
from collections.abc import Generator
from pathlib import Path
from typing import Final

from benchmark import Benchmarked

from helper import print

GLOB_PATTERN: Final = "problem_*.py"


def get_problems() -> Generator[Benchmarked, None, None]:
    """
    Returns a generator of all the Benchmarked
    decorated problems in the current directory

    Returns:
        Generator[Benchmarked, None, None]: Benchmarked problems
    """
    for path in Path(__file__).parent.glob(GLOB_PATTERN):
        stem = path.stem
        yield importlib.import_module(stem).__dict__[stem]


def main():
    total_time: float = 0
    problems: list[Benchmarked] = [*get_problems()]

    for problem in problems:
        problem()
        total_time += problem.elapsed()
    print(
        f"Total time taken for all {len(problems)} problems: {total_time} milliseconds"
    )


if __name__ == "__main__":
    main()
