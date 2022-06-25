from __future__ import annotations

from collections.abc import Callable
from time import perf_counter
from typing import Generic, Literal, ParamSpec, TypeVar

from .colorize import time_format
from .typeshack import MISSING as _MISSING
from .typeshack import All, Slots

__all__: All = ("Benchmarked",)

P = ParamSpec("P")
Q = TypeVar("Q")
R = TypeVar("R")


def _format_benchmark(name, elapsed, result):
    colorized_time = time_format(elapsed)
    return f"{name} took {colorized_time} milliseconds to be completed and returned '{result}'"


class Benchmarked(Generic[P, R]):
    """
    The class used to benchmark problem execution time
    Example usage :

    ```
    >>> @Benchmarked
    ... def foo():
    ...     time.sleep(2)
    ...     return "This works!"
    ```

    A function named foo was wrapped by the Benchmarked class
    and was reassigned to an instance of the class
    This instance can be called like:

    ```
    >>> foo()
    foo took 2010.2348001673818 milliseconds to be completed and returned 'This works!'
    'This works!'
    ```

    And has methods like `elapsed` and `result` to retrieve the time
    taken for execution and the returned result, respectively.

    ```
    >>> foo.elapsed()
    2010.2348001673818
    >>> foo.result()
    'This works!'
    ```

    It can also retrieve the original function as required

    ```
    >>> original_func = foo.function
    >>> original_func
    <function foo at 0x0000022F2F421510>
    >>> original_func()
    'This works!'
    ```
    """

    __slots__: Slots = (
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
        self.__result: R | Literal[_MISSING] = _MISSING

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> R:
        """
        Calls the benchmarked function and returns the result
        also sets the elapsed time, result and then prints the human friendly
        output

        Calling the instance is roughly equivalent to:
        >>> obj = Benchmarked(func)
        >>> obj.benchmark(*args, **kwargs)
        >>> obj.show_performance()

        Args:
            P: The same arguments as the wrapped function

        Returns:
            R: The result of the benchmarked function
        """
        ret: R = self.benchmark(*args, **kwargs)
        self.show_performance()
        return ret

    def __repr__(self) -> str:
        """
        Returns the representation of the benchmarked function

        Returns:
            str: The representation of the benchmarked function
                 with the name of the function
        """
        cls_name = self.__class__.__name__
        func_name = self.__func.__name__
        return f"{cls_name}({func_name})"

    def __str__(self) -> str:
        """
        Returns the string representation of the benchmarked function
        with the name of the function and the elapsed time
        and result if the benchmark has been run

        Returns:
            str: The info of the benchmark
        """
        name: str = self.__func.__name__
        elapsed: float | None = self.due
        result: R | Literal[_MISSING] = self.__result

        if elapsed is None:
            return f"{name}: not measured"
        return _format_benchmark(name=name, elapsed=elapsed, result=result)

    def show_performance(self) -> None:
        """
        Prints the function name, elapsed time and result
        in a human friendly format
        """
        print(self)

    def benchmark(self, *args: P.args, **kwargs: P.kwargs) -> R:
        """
        Benchmarks the function and returns the result
        also sets the elapsed time and result

        Args:
            P: The same arguments as the wrapped function

        Returns:
            R: The result of the benchmarked function
        """
        start: float = perf_counter()
        self.__result = self.__func(*args, **kwargs)
        self.__elapsed = (perf_counter() - start) * 1000
        return self.__result

    def result(self, sentinel: Q = _MISSING) -> R | Q:
        """
        Returns the result of the benchmarked function
        if the benchmark has not been run (ie, object not called)
        then the sentinel is returned if provided
        else a ValueError is raised

        Args:
            sentinel (Q, optional): Defaults to MISSING.

        Returns:
            R | Q: The result of the benchmarked function or the sentinel if provided

        Raises:
            ValueError: If the benchmark has not been run (ie, object not called)
                        and an sentinel value was not provided
        """
        if self.due is None:
            if sentinel is _MISSING:
                msg = "Benchmarked object not called and an sentinel value has not been provided"
                raise ValueError(msg)
            return sentinel
        return self.__result

    def elapsed(self) -> float:
        """
        Returns the elapsed time in milliseconds

        Returns:
            float: The elapsed time in milliseconds

        Raises:
            ValueError: If the benchmark has not been run (ie, object not called)
        """
        if self.due is None:
            raise ValueError("Benchmarked function has not been called")
        return self.due

    @property
    def function(self) -> Callable[P, R]:
        """
        Returns the function that is wrapped by this class

        Returns:
            Callable[P, R]: The wrapped function
        """
        return self.__func

    @property
    def due(self) -> float | None:
        """
        Returns the elapsed time in milliseconds
        or None if the benchmark has not been run
        unlike `elapsed` which raises an error if the benchmark has not been run

        Returns:
            float | None: The elapsed time in milliseconds or None
        """
        return self.__elapsed
