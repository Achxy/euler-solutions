from __future__ import annotations

from collections.abc import Awaitable, Iterator
from types import CoroutineType
from enum import Enum
from typing import TYPE_CHECKING, Callable, ClassVar, Coroutine, Final, Literal, TypeVar

if TYPE_CHECKING:
    from typing import ParamSpec, TypeAlias

    from .benchmark import Benchmarked

    Params = ParamSpec("Params")
else:
    # During runtime
    Benchmarked = object()
    Params = TypeVar("Params")


class _Sentinel(Enum):
    """
    Single member enum for static typecheckers to validate
    code, this is necessitated due to the fact that
    assigning sentinels to value returned by object()
    causes incorrect type inference.

    See, https://peps.python.org/pep-0661/
    """

    MISSING = object()


Q = TypeVar("Q")
Result = TypeVar("Result")
CoVarCoroFunction = TypeVar(
    "CoVarCoroFunction", bound=Callable[..., CoroutineType], covariant=True
)

All: TypeAlias = Final[tuple[str, ...]]
OptionalFloat: TypeAlias = float | None
Slots = ClassVar[tuple[str, ...]]

MISSING: Literal[_Sentinel.MISSING] = _Sentinel.MISSING
Coro: TypeAlias = Coroutine[None, None, Result]
Func: TypeAlias = Callable[Params, Result]
CoroFunc: TypeAlias = Callable[Params, Coro]
AnyFunc: TypeAlias = Func | CoroFunc
CanBeFunctionOrCoro: TypeAlias = Func | Coro
CouldBeMissing: TypeAlias = Result | Literal[MISSING]

Problems: TypeAlias = Iterator[Benchmarked]
