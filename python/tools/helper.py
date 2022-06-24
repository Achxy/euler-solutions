from pathlib import Path
from typing import Final

from .typeshack import All

__all__: All = ("form_path",)
PATH: Final[Path] = Path(__file__).parents[2] / "data"


def form_path(filename: str) -> Path:
    return PATH / filename
