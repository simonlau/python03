# Type Aliases

> Sources: The Python Typing Team, Unknown
> Raw: [2026-10-29-type-aliases](../../raw/type-aliases/2026-10-29-type-aliases.md)
> Updated: 2026-10-29

## Overview

Python supports type aliases — names bound to type hints that improve readability and clarify intent in type-annotated code. Type aliases may be defined in three ways: simple variable assignments, `typing.TypeAlias`, and the `type` statement (Python 3.12 and higher). Alias names should be capitalized, since they represent user-defined types, which (like user-defined classes) are conventionally spelled that way. Anything acceptable as a type hint is acceptable in a type alias.

## Defining Type Aliases

### Simple assignment

The simplest form is a plain variable assignment:

```
Url = str

def retry(url: Url, retry_count: int) -> None: ...
```

### `typing.TypeAlias`

The explicit `TypeAlias` annotation clearly differentiates between typed global expressions, untyped global expressions, and type aliases:

```
from typing import TypeAlias

Url: TypeAlias = str

def retry(url: Url, retry_count: int) -> None: ...
```

`TypeAlias` avoids classifying the nature of an assignment based on the type of the value, which prevents assignments from breaking type checking when an annotation is added. For backwards compatibility, type checkers should support both implicit (`x = int`) and explicit (`x: TypeAlias = int`) forms simultaneously.

### `type` statement (Python 3.12+)

The `type` statement creates explicitly generic type aliases:

```
type ListOrSet[T] = list[T] | set[T]
```

Type parameters declared as part of a generic type alias are valid only when evaluating the right-hand side. Type checkers should restrict the right-hand expression to forms allowed within type annotations — call expressions, ternary operators, arithmetic and comparison operators, etc., should be flagged as errors. Traditional type variables created with an explicit `TypeVar` constructor call are not allowed:

```
T = TypeVar("T")
type MyList = list[T]  # Type checker error: traditional type variable usage
```

## `NewType`

`NewType` creates simple unique types with almost zero runtime overhead, avoiding the overhead of defining a full `class` when you only need a distinct logical type:

```
UserId = NewType('UserId', int)

def name_by_id(user_id: UserId) -> str:
    ...

UserId('user')          # Fails type check
name_by_id(42)          # Fails type check
name_by_id(UserId(42))  # OK

num = UserId(5) + 1     # type: int
```

`NewType` accepts exactly two arguments: a name for the new unique type and a base class (a proper class or another `NewType` type, not a type construct like `Union`). The returned callable accepts only one argument. `isinstance`, `issubclass`, and subclassing fail for `NewType` types since the returned object is not a class.

Example with a custom base class:

```
class PacketId:
    def __init__(self, major: int, minor: int) -> None:
        self._major = major
        self._minor = minor

TcpPacketId = NewType('TcpPacketId', PacketId)

packet = PacketId(100, 100)
tcp_packet = TcpPacketId(packet)  # OK

tcp_packet = TcpPacketId(127, 0)  # Fails in type checker and at runtime
```

## Comparison with a Real Class

Defining a dedicated class (e.g. `class UserId(int): ...`) introduces runtime overhead. `NewType` is the lightweight alternative when you only need static type checking to catch logical errors such as mixing up IDs of different kinds.

## See Also
