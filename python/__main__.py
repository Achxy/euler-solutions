from __future__ import annotations

import importlib
from collections.abc import Generator, Iterable
from pathlib import Path
from typing import TypeAlias, TypeVar

from benchmark import Benchmarked

BenchmarkMap: TypeAlias = dict[str, Benchmarked]
IGNORE: tuple[str, ...] = ("benchmark.py", "__main__.py", "helper.py")
T = TypeVar("T", bound=Benchmarked)


def get_all_files(directory: Path, ignore=IGNORE) -> list[Path]:
    """
    Returns a list of all files in the given directory.
    The mentioned in `ignore` are ignored from the result

    Args:
        directory (Path): The directory to search for files
        ignore (tuple, optional): The files to ignore. Defaults to ("benchmark.py", "__main__.py").

    Returns:
        list[Path]: A list of all files in the given directory
    """
    files: list[Path] = [file for file in directory.iterdir() if file.is_file() and file.name not in ignore]
    return files


def load_all_files_in_directory(directory: Path) -> BenchmarkMap:
    """
    Loads all files in the given directory and returns a map of the loaded functions
    The value of the map is the function that was loaded with same name as the file
    ie, problem_1.py -> problem_1 function

    Args:
        directory (Path): The directory to search for files

    Returns:
        BenchmarkMap: A map of problems to their benchmarked functions
    """
    files: list[Path] = get_all_files(directory)
    benchmap: BenchmarkMap = {}
    for file in files:
        module = importlib.import_module(file.stem)
        benchmap[file.stem] = module.__dict__[file.stem]
    return benchmap


def as_completed(functions: Iterable[T]) -> Generator[T, None, None]:
    """
    Returns a generator that yields the functions in the given iterable in order
    This calls the constituent functions and returns it so that elapsed time can be calculated
    args:
        functions (Iterable[T]): The functions to yield

    Returns:
        Generator[T, None, None]: A generator that yields the functions in the given iterable in order
    """
    for fn in functions:
        fn()
        yield fn


def start() -> None:
    """
    Entry point for executing all the programs in the directory
    """
    functions: BenchmarkMap = load_all_files_in_directory(Path(__file__).parent)
    elapsed: float = 0
    problem_count: int = len(functions)
    for fn in as_completed(functions.values()):
        elapsed += fn.elapsed()
    print(f"Total time taken for all {problem_count} problems: {elapsed} milliseconds")


if __name__ == "__main__":
    start()
