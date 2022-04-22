# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

from pathlib import Path as _Path

_DATA_DIR = _Path(__file__).resolve().parent.parent / "data"


def data(problem):
    prefix = f"p{problem:03d}_"
    for path in _DATA_DIR.iterdir():
        if path.name.startswith(prefix):
            return path.read_text()
    raise FileNotFoundError(f"no data file for problem {problem}")
