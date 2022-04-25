from __future__ import annotations

import importlib
import time
from pathlib import Path
from typing import Callable, TypeAlias

FnMap: TypeAlias = dict[str, Callable[..., int]]


def get_all_files(directory: Path, ignore=("benchmark.py", "__main__.py")) -> list[Path]:
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


def load_all_files_in_directory(directory: Path) -> FnMap:
    """
    Loads all files in the given directory and returns a map of the loaded functions
    The value of the map is the function that was loaded with same name as the file
    ie, problem_1.py -> problem_1 function

    Args:
        directory (Path): The directory to search for files

    Returns:
        FnMap: A map of problems to their functions
    """
    files: list[Path] = get_all_files(directory)
    functions: FnMap = {}
    for file in files:
        module = importlib.import_module(file.stem)
        functions[file.stem] = module.__dict__[file.stem]
    return functions


def start() -> None:
    """
    Entry point for executing all the programs in the directory
    """
    s_time: float = time.perf_counter()
    functions: FnMap = load_all_files_in_directory(Path(__file__).parent)
    for fn in functions.values():
        fn()  # Results should be printed because of the `measure` decorator in the benchmark.py file
    print(
        (
            f"Total time for {len(functions)} problems to be "
            f"completed: {(time.perf_counter() - s_time) * 1000} milliseconds"
        )
    )


if __name__ == "__main__":
    start()
