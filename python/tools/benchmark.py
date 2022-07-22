from __future__ import annotations

from collections.abc import Awaitable, Callable, Coroutine, Generator
from functools import wraps
from inspect import iscoroutinefunction
from time import perf_counter
from typing import Final, Generic, Literal, overload, Any
from typing_extensions import reveal_type

from .colorize import time_format
from .helper import get_name, repr_fmt
from .typeshack import MISSING as _MISSING
from .typeshack import (
    All,
    OptionalFloat,
    Params,
    Q,
    Result,
    Slots,
)

__all__: All = ("Benchmarked",)

ANONYMOUS_CALLABLE: Final[str] = "<anonymous_callable>"


def _format_benchmark(name: str, elapsed: float, result: Any):
    colorized_time = time_format(elapsed)
    return f"{name} took {colorized_time} milliseconds to be completed and returned '{result}'"


class Benchmarked(Generic[Params, Result]):
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
        "_sub_or_co_routine",
        "_original_coro",
        "_elapsed",
        "_result",
    )

    @overload
    def __init__(
        self,
        syncfunc_or_coro: Callable[Params, Result],
        original_corofunc: None,
    ) -> None:
        ...

    @overload
    def __init__(
        self,
        syncfunc_or_coro: Awaitable[Result],
        original_corofunc: Callable[Params, Awaitable[Result]],
    ) -> None:
        ...

    def __init__(self, syncfunc_or_coro, original_corofunc) -> None:
        """
        Initializes the benchmarked function

        Args:
            func (Callable[P, R]): The function to benchmark
        """
        self._sub_or_co_routine = syncfunc_or_coro
        self._original_coro = original_corofunc
        self._elapsed: OptionalFloat = None
        self._result: Result | Literal[_MISSING] = _MISSING

    def __call__(self, *args: Params.args, **kwargs: Params.kwargs) -> Result:
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
        ret: Result = self.benchmark(*args, **kwargs)
        self.show_performance()
        return ret

    def __await__(self) -> Generator[Awaitable[Result], None, Result]:
        if not self.is_coroutine:
            raise TypeError("Cannot be awaited unless instantiated with a coroutine")
        ret: Result = yield from self._sub_or_co_routine.__await__()
        return ret

    def __repr__(self) -> str:
        """
        Returns the representation of the benchmarked function

        Returns:
            str: The representation of the benchmarked function
                 with the name of the function
        """
        cls = type(self)
        function_name = get_name(self.function, ANONYMOUS_CALLABLE)
        return repr_fmt(cls, function_name)

    def __str__(self) -> str:
        """
        Returns the string representation of the benchmarked function
        with the name of the function and the elapsed time
        and result if the benchmark has been run

        Returns:
            str: The info of the benchmark
        """
        name: str = get_name(self.function, ANONYMOUS_CALLABLE)
        elapsed: OptionalFloat = self.due
        result: Result | Literal[_MISSING] = self._result

        if elapsed is None:
            return f"{name}: not measured"
        return _format_benchmark(name=name, elapsed=elapsed, result=result)

    def show_performance(self) -> None:
        """
        Prints the function name, elapsed time and result
        in a human friendly format
        """
        print(self)

    def benchmark(self, *args: Params.args, **kwargs: Params.kwargs) -> Result:
        """
        Benchmarks the function and returns the result
        also sets the elapsed time and result

        Args:
            P: The same arguments as the wrapped function

        Returns:
            R: The result of the benchmarked function
        """
        if self.is_coroutine:
            raise TypeError("Coroutine object not callable, did you mean to await it?")
        start: float = perf_counter()
        self._result = self._sub_or_co_routine(*args, **kwargs)
        self._elapsed = (perf_counter() - start) * 1000
        return self._result

    def result(self, sentinel: Q = _MISSING) -> Result | Q:
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
        return self._result

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
    def is_coroutine(self) -> bool:
        return self._original_coro is not None

    @property
    def function(self) -> Callable[Params, Result]:
        """
        Returns the function that is wrapped by this class

        Returns:
            Callable[P, R]: The wrapped function
        """
        if self.is_coroutine:
            return self._original_coro
        return self._sub_or_co_routine

    @property
    def due(self) -> OptionalFloat:
        """
        Returns the elapsed time in milliseconds
        or None if the benchmark has not been run
        unlike `elapsed` which raises an error if the benchmark has not been run

        Returns:
            float | None: The elapsed time in milliseconds or None
        """
        return self._elapsed


def _corofunc_wrapper(
    corofunc: Callable[Params, Awaitable[Result]]
) -> Callable[Params, Benchmarked[Params, Result]]:
    # It is better not to use functools.wraps here
    # to avoid confusion
    def benchmark_wrapper(
        *args: Params.args, **kwargs: Params.kwargs
    ) -> Benchmarked[Params, Result]:
        coro: Awaitable[Result] = corofunc(*args, **kwargs)
        return Benchmarked(coro, original_corofunc=corofunc)

    return benchmark_wrapper


def benchmark(
    anyfunc: Callable[Params, Result] | Callable[Params, Coroutine[None, None, Result]]
) -> Callable[Params, Benchmarked[Params, Result]] | Benchmarked[Params, Result]:
    if iscoroutinefunction(anyfunc):
        return _corofunc_wrapper(anyfunc)  # type: ignore
    if callable(anyfunc):
        return Benchmarked(anyfunc, original_corofunc=None)  # type: ignore
    msg = f"Expected callable, got {anyfunc!r} instead"
    raise TypeError(msg)
