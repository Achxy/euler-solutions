from pathlib import Path
from typing import Final

from .typeshack import All

__all__: All = ("form_path",)
PATH: Final[Path] = Path(__file__).parents[2] / "data"


def form_path(filename: str) -> Path:
    """
    Form path by concatenating the path below 2 levels
    to .... / "data" / filename


    Args:
        filename (str): File name to form path to

    Returns:
        Path: The path formed by concatenation
    """
    return PATH / filename
