from inspect import isclass
from pathlib import Path
from re import sub
from typing import Any, Final

from .typeshack import All

__all__: All = (
    "form_path",
    "clean_whitespaces",
)

PATH: Final[Path] = Path(__file__).parents[2] / "data"
COMMA_SEP: Final[str] = ", "


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


def get_name(obj: Any, replace_with: str | None = None) -> str:
    if hasattr(obj, "__name__"):
        return obj.__name__
    if replace_with is not None:
        return replace_with
    raise TypeError(f"{obj!r} has no attribute __name__")


def _get_args_and_kwargs_fmt(a: tuple[Any, ...], k: dict[Any, Any]) -> str:
    args_fmt = COMMA_SEP.join(repr(q) for q in a)
    kwargs_fmt = COMMA_SEP.join(f"{k}={repr(v)}" for k, v in k.items())
    return args_fmt + COMMA_SEP + kwargs_fmt if a and k else args_fmt + kwargs_fmt


def repr_fmt(cls: type, *args: Any, **kwargs: Any) -> str:
    if not isclass(cls):
        msg = f"Expected {cls!r} to be type (class) instance, got {type(cls)} instead"
        raise TypeError(msg)
    class_name = get_name(cls)
    return f"{class_name}({_get_args_and_kwargs_fmt(args, kwargs)})"
