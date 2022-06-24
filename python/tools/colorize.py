from typing import Any

from colorama import Fore, Style

COLOR_RANGE: dict[range, str] = {
    range(0, 140): Fore.GREEN,
    range(140, 300): Fore.YELLOW,
}


def colorize(obj: Any, color) -> str:
    """
    Takes in an object of any instance, calls __str__
    on it and then concatenates ansi escape sequence to it
    which is provided by the `color` argument

    Args:
        obj (Any): An object of any instances
        color: Ansi escape sequence

    Returns:
        str: Concatenated result
    """
    return color + str(obj) + Style.RESET_ALL


def time_format(number: float, fallback: str = Fore.RED) -> str:
    """
    Used for pretty formatting time
    fallback is used if `number` argument is not present in the color
    rage hashmap

    Args:
        number (float): The time which needs to be formatted
        fallback (str, optional): fallback if number wasn't in the range
                                  provided in the hashmap.
                                  Defaults to Fore.RED.

    Returns:
        str: formatted time by concatenating ansi escape sequence
    """
    for span in COLOR_RANGE.keys():
        num_approx = round(number)
        if num_approx in span:
            return colorize(number, COLOR_RANGE[span])
    return colorize(number, fallback)
