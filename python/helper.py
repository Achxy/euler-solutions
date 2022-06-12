from pathlib import Path


__all__: tuple[str] = ("form_path",)

PATH: Path = Path(__file__).parent.parent / "data"


def form_path(filename) -> Path:
    return PATH / filename
