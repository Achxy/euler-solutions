from pathlib import Path

__all__: tuple[str, ...] = (
    "form_path",
    "print",
)

PATH: Path = Path(__file__).parent.parent / "data"


try:
    from rich import print
except ImportError:
    print = __builtins__.print


def form_path(filename) -> Path:
    return PATH / filename
