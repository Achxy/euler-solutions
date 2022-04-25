from time import perf_counter
from typing import Callable, ParamSpec, TypeVar

R = TypeVar("R")
P = ParamSpec("P")


def measure(func: Callable[P, R]) -> Callable[P, R]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        start: float = perf_counter()
        result: R = func(*args, **kwargs)
        print(
            (
                f"{func.__name__} took {(perf_counter() - start) * 1000} "
                f"milliseconds to be completed and returned {result}"
            )
        )
        return result

    return wrapper
