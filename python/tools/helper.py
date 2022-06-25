from pathlib import Path
from re import sub
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


def clean_whitespaces(string: str) -> str:
    """
    Removes whitespaces characters such as new line, return carriage, form feed
    et cetera from a given string

    Args:
        string (str): The string to remove the whitespace from

    Returns:
        str: The new string returned with whitespaces removed
    """
    return sub(r"\s+", "", string)
