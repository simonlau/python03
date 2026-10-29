# Python Tuple

> Sources: Leodanis Pozo Ramos (Real Python), 2023-10-04
> Raw: [python-tuple-data-type-deep-dive](../../raw/python-collections/python-tuple-data-type-deep-dive.md)
> Updated: 2026-10-29

## Overview

Python’s `tuple` is a built-in data type for creating **immutable sequences** of values. Items can be of any type, making tuples useful for storing heterogeneous data such as database records. Tuples are ordered, lightweight, indexable (zero-based), immutable, heterogeneous, nestable, iterable, sliceable, combinable, and hashable (when all items are immutable). They are commonly called containers or collections.

## Constructing Tuples

### Tuple literals

A tuple is a comma-separated series of objects; the commas are required, the parentheses are optional in most cases:

```
(item_0, item_1, ..., item_n)
```

Examples:

```
>>> jane = ("Jane Doe", 25, 1.75, "Canada")
>>> point = (2, 7)
>>> pen = (2, "Solid", True)
```

An empty tuple requires parentheses: `()`. A single-item tuple requires a trailing comma: `(42,)` or `"Hello",`. Without the trailing comma, `(42)` is just an `int`, not a tuple — a common gotcha.

### `tuple()` constructor

Build a tuple from any iterable (list, set, dict, string, generator):

```
>>> tuple(["Jane Doe", 25, 1.75, "Canada"])
('Jane Doe', 25, 1.75, 'Canada')
>>> tuple("Pythonista")
('P', 'y', 't', 'h', 'o', 'n', 'i', 's', 't', 'a')
>>> tuple(x**2 for x in range(10))
(0, 1, 4, 9, 16, 25, 36, 49, 64, 81)
```

`tuple()` with no arguments returns an empty tuple. Sets are accepted but unordered, so the resulting order is not guaranteed. Potentially infinite iterators will hang the constructor.

## Accessing Items

Use zero-based indexing; indexing is O(1):

```
>>> jane = ("Jane Doe", 25, 1.75, "Canada")
>>> jane[0]
'Jane Doe'
>>> jane[-1]
'Canada'
```

Out-of-range indices raise `IndexError`. Negative indices count from the right (`-1` is the last item). Nested sequences are accessed by chaining indices:

```
>>> employee = ("John", 35, "Python Developer", ("Django", "Flask", "FastAPI"))
>>> employee[-1][0]
'Django'
```

## Slicing

```
tuple_object[start:stop:step]
```

All indices are optional (`start` defaults to `0`, `stop` to `len(tuple)`, `step` to `1`):

```
>>> days[:5]
('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
>>> days[5:]
('Saturday', 'Sunday')
```

Slicing works like lists except for in-place mutations.

## Immutability

Tuples cannot be changed in place — no item assignment, no growing or shrinking, no `del` on items:

```
>>> jane[3] = "United States"
TypeError: 'tuple' object does not support item assignment
```

Tuples can store mutable objects, and those mutable objects can still be changed in place even when nested in a tuple:

```
>>> student_info = ("Linda", 18, ["Math", "Physics", "History"])
>>> student_info[2][2] = "Computer science"
```

Tuples can be dictionary keys only when all items are hashable; tuples containing lists raise `TypeError: unhashable type: 'list'`.

## Packing and Unpacking

Packing: `point = x, y, z`. Unpacking:

```
>>> x, y, z = (7, 14, 21)
```

The number of variables must match the number of items, otherwise `ValueError`. Swap values without a temporary variable:

```
>>> a, b = b, a
```

The `*` operator collects extra values into a list:

```
>>> numbers = (1, 2, 3, 4, 5)
>>> *head, last = numbers
>>> head
[1, 2, 3, 4]
>>> last
5
```

Merge tuples with `*`:

```
>>> (*("John", "Doe"), *("john@example.com", "55-555-5555"))
('John', 'Doe', 'john@example.com', '55-555-5555')
```

## Returning Tuples From Functions

A comma-separated `return` creates a tuple:

```
>>> def find_extremes(iterable):
...     data = tuple(iterable)
...     if len(data) == 0:
...         raise ValueError("input iterable must not be empty")
...     return min(data), max(data)
...
>>> find_extremes([3, 4, 2, 6, 7, 1, 9])
(1, 9)
```

The built-in `divmod()` returns a quotient/remainder tuple that can be unpacked.

## Copies

Shallow copies (slicing, `copy.copy()`) create aliases, not copies — `id()` stays the same. Because tuples are immutable, copies are usually unnecessary. `copy.deepcopy()` creates a new tuple object; changes to mutable objects in the copy don’t affect the original.

## Concatenation and Repetition

```
>>> ("John", 35) + ("Computer science", ("Python", "Django"))
('John', 35, 'Computer science', ('Python', 'Django'))
>>> (1, 2, 3) * 3
(1, 2, 3, 1, 2, 3, 1, 2, 3)
```

You can only concatenate tuple with tuple (mixing with a list raises `TypeError`). Augmented `+=` and `*=` always create new tuple objects because of immutability.

## Reversing and Sorting

```
>>> tuple(reversed(days))
>>> days[::-1]                      # new reversed tuple
>>> sorted(numbers)                 # returns a list, not a tuple
>>> sorted(numbers, reverse=True)
>>> sorted(fruits, key=lambda fruit: fruit[1])
```

`reversed()` returns an iterator; `sorted()` returns a list. Sorting heterogeneous tuples with `<` or `>` may raise `TypeError` if items can’t be compared.

## Traversing

Use `for` loops (with optional tuple unpacking and `enumerate()`), comprehensions, generator expressions, `map()`, or `filter()`. Generator expressions are more memory-efficient than comprehensions when building a new tuple via `tuple()`.

## Other Features

Only two public methods: `.count()` and `.index()`. Membership tests with `in`/`not in` are O(n); for frequent lookups, prefer sets (O(1)). `len()` is O(1). Comparisons use lexicographical ordering (item-by-item).

## Gotchas

- Forgetting the trailing comma in one-item tuples: `(42)` is an `int`, `(42,)` is a tuple.
- Tuples containing mutable items are unhashable and can’t be dictionary keys.

## Alternatives to Built-in Tuples

When numeric indices are error-prone, use named-field alternatives:

- **`collections.namedtuple`** — tuple subclass with dot-notation field access; immutable; subclass of `tuple`.
- **`typing.NamedTuple`** — typed version with type hints and default values.
- **`dataclasses.dataclass`** — similar but mutable by default; pass `frozen=True` for immutability.

## When to Use Tuples

Use tuples to ensure data integrity, reduce memory consumption, and improve performance. Concrete use cases: associating two or more values, representing database records, providing multi-value dictionary keys.

## See Also

- [Mastering Python Collections](mastering-python-collections.md) — broader treatment of Python collections including lists, sets, dicts, generators, and comprehensions.
- [Command-Line Arguments](../command-line-arguments/command-line-arguments.md) — Exercise 0 introduces `sys.argv` as a list.
- [Walrus Operator](../assignment-expressions/walrus-operator.md) — assignment expressions usable inside comprehensions.
