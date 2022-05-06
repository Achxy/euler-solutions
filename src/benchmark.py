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
    """
    Single member enum for sentinel values
    More acceptable for static typecheckers
    """

    MISSING = object()


MISSING = _Sentinel.MISSING


class Benchmarked(Generic[P, R]):
    """
    The class used to benchmark problem execution time
    """

    __slots__: ClassVar[tuple[str, ...]] = (
        "__func",
        "__elapsed",
        "__result",
    )

    def __init__(self, func: Callable[P, R]) -> None:
        """
        Initializes the benchmarked function

        Args:
            func (Callable[P, R]): The function to benchmark
        """
        self.__func: Callable[P, R] = func
        self.__elapsed: float | None = None
        self.__result: R | Literal[MISSING] = MISSING

    def show_performance(self) -> None:
        """
        Prints the function name, elapsed time and result
        in a human friendly format
        """
        name: str = self.__func.__name__
        elapsed: float | None = self.__elapsed
        result: R | Literal[MISSING] = self.__result

        if result is MISSING:
            return print(f"{name}: not measured")

        print(f"{name} took {elapsed} milliseconds to be completed and returned '{result}'")

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> R:
        """
        Calls the benchmarked function and returns the result
        also sets the elapsed time and result

        Returns:
            R: The result of the benchmarked function
        """
        start: float = perf_counter()
        self.__result = self.__func(*args, **kwargs)
        self.__elapsed = (perf_counter() - start) * 1000
        self.show_performance()
        return self.__result

    def result(self, sentinel: Q = MISSING) -> R | Q:
        """
        Returns the result of the benchmarked function
        if the benchmark has not been run (ie, object not called)
        then the sentinel is returned defaulting to `MISSING`

        Args:
            sentinel (Q, optional): Defaults to MISSING.

        Returns:
            R | Q: The result of the benchmarked function or the sentinel
        """
        if self.__result is MISSING:
            return sentinel
        return self.__result

    def elapsed(self) -> float:
        """
        Returns the elapsed time in milliseconds


        Raises:
            ValueError: If the benchmark has not been run (ie, object not called)

        Returns:
            float: The elapsed time in milliseconds
        """
        if self.__elapsed is None:
            raise ValueError("Benchmarked function has not been called")
        return self.__elapsed

    @property
    def function(self) -> Callable[P, R]:
        """
        Returns the function that is wrapped by this class

        Returns:
            Callable[P, R]: The wrapped function
        """
        return self.__func
