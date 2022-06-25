from __future__ import annotations

import importlib
from pathlib import Path
from typing import Final

from tools.typeshack import Problems

GLOB_PATTERN: Final[str] = "problem_*.py"
PARENT_DIR: Final[Path] = Path(__file__).parent


def get_problems() -> Problems:
    """
    Returns a generator of all the Benchmarked
    decorated problems in the current directory

    Returns:
        Problems: Benchmarked problems
    """
    for path in PARENT_DIR.glob(GLOB_PATTERN):
        stem: str = path.stem
        yield importlib.import_module(stem).__dict__[stem]


def execute_problems(problems: Problems) -> None:
    """
    Calls each Benchmarked instances from a given iterator
    Then prints the total time taken to finish calling all instances

    Args:
        problems (Problems): An iterator containing Benchmarked class instances
    """
    total_time: float = 0
    probs = [*problems]
    for problem in probs:
        problem()
        total_time += problem.elapsed()
    print(f"Total time taken for all {len(probs)} problems: {total_time} milliseconds")


def main() -> None:
    """
    Entry point function for computing all the problems
    """
    problems: Problems = get_problems()
    execute_problems(problems)


if __name__ == "__main__":
    main()
