from typing import Any
from colorama import Fore, Style


COLOR_RANGE: dict[range, str] = {
    range(0, 140): Fore.GREEN,
    range(140, 300): Fore.YELLOW,
}


def colorize(obj: Any, color: str = "") -> str:
    return color + str(obj) + Style.RESET_ALL


def time_format(number: float, fallback: str = Fore.RED) -> str:
    for span in COLOR_RANGE.keys():
        num_approx = round(number)
        if num_approx in span:
            return colorize(number, COLOR_RANGE[span])
    return colorize(number, fallback)
