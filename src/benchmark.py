from __future__ import annotations

from collections.abc import Callable
from enum import Enum
from time import perf_counter
from typing import ClassVar, Final, Generic, Literal, ParamSpec, TypeVar

__all__: Final[tuple[str]] = ("Benchmarked",)

P = ParamSpec("P")
Q = TypeVar("Q")
R = TypeVar("R")


class _Sentinel(Enum):
    MISSING = object()


MISSING = _Sentinel.MISSING


class Benchmarked(Generic[P, R]):
    __slots__: ClassVar[tuple[str, ...]] = (
        "__func",
        "__elapsed",
        "__result",
    )

    def __init__(self, func: Callable[P, R]) -> None:
        self.__func: Callable[P, R] = func
        self.__elapsed: float | None = None
        self.__result: R | Literal[MISSING] = MISSING

    def show_performance(self) -> None:
        name: str = self.__func.__name__
        elapsed: float | None = self.__elapsed
        result: R | Literal[MISSING] = self.__result

        if result is MISSING:
            return print(f"{name}: not measured")

        print(f"{name} took {elapsed} milliseconds to be completed and returned '{result}'")

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> R:
        start: float = perf_counter()
        self.__result = self.__func(*args, **kwargs)
        self.__elapsed = (perf_counter() - start) * 1000
        self.show_performance()
        return self.__result

    def result(self, sentinel: Q = MISSING) -> R | Q:
        if self.__result is MISSING:
            return sentinel
        return self.__result

    def elapsed(self) -> float:
        if self.__elapsed is None:
            raise ValueError("Benchmarked function has not been called")
        return self.__elapsed

    @property
    def function(self) -> Callable[P, R]:
        return self.__func
