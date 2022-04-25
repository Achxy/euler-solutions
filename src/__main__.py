from __future__ import annotations

import importlib
import time
from pathlib import Path
from typing import Callable, TypeAlias

FnMap: TypeAlias = dict[str, Callable[..., int]]


def get_all_files(directory: Path, ignore=("benchmark.py", "__main__.py")) -> list[Path]:
    files: list[Path] = [file for file in directory.iterdir() if file.is_file() and file.name not in ignore]
    return files


def load_all_files_in_directory(directory: Path) -> FnMap:
    files: list[Path] = get_all_files(directory)
    functions: FnMap = {}
    for file in files:
        module = importlib.import_module(file.stem)
        functions[file.stem] = module.__dict__[file.stem]
    return functions


def start():
    s_time: float = time.perf_counter()
    functions: FnMap = load_all_files_in_directory(Path(__file__).parent)
    for fn in functions.values():
        fn()  # Results should be printed because of the `measure` decorator in the benchmark.py file
    print(f"Total time for {len(functions)} problems to be completed: {time.perf_counter() - s_time}")


if __name__ == "__main__":
    start()
