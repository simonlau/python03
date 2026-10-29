# Python Set

> Sources: Leodanis Pozo Ramos (Real Python), 2026-10-23
> Raw: [python-sets-deep-dive](../../raw/python-collections/python-sets-deep-dive.md)
> Updated: 2026-10-29

## Overview

Python’s `set` is a built-in data type that creates an unordered collection of unique, hashable elements. Sets are mutable (you can add or remove elements), unordered (no specific order maintained), and enforce uniqueness (duplicates removed automatically). They are useful for set operations, removing duplicates, running efficient membership tests, and more.

Python implements sets as hash tables, so membership tests with `in`/`not in` are exceptionally efficient compared to lists.

## Constructing Sets

### Set literals

Define a set with comma-separated hashable objects within curly braces `{}`:

```
{obj_0[, obj_1, ..., obj_n]}
```

Examples:

```
>>> hex_colors = {"#33FF57", "#3357FF", "#F1C40F", "#E74C3C"}
>>> {2, 4, 6, 8, 10, 8, 2}
{2, 4, 6, 8, 10}
```

**Note:** You can’t use a literal to create an empty set — `{}` creates a dictionary. Set literals add each object as a distinct element and do not unpack iterables (a tuple added as an element stays a tuple).

### `set()` constructor

Use the constructor to build a set from any iterable, or to create an empty set:

```
>>> set()
set()
>>> set([1, 2, 2, 3, 4, 4, 5])
{1, 2, 3, 4, 5}
>>> set("Python")
{'y', 'P', 'o', 't', 'n', 'h'}
```

There’s a subtle difference between the constructor and literals: `set("Hello!")` unpacks the string into characters (`{'H', 'l', 'e', '!', 'o'}`), whereas `{"Hello!"}` keeps it as a single element (`{'Hello!'}`).

### Set comprehensions

Set comprehensions create a set by evaluating an expression over an iterable, automatically removing duplicates:

```
{expression for member in iterable [if condition]}
```

Example — cleaning usernames:

```
>>> {name.lower().strip() for name in usernames}
{'bob', 'alice', 'john', 'charlie'}
```

## Elements Must Be Hashable

Set elements must be hashable. Tuples of hashable values can be set elements, but lists, dictionaries, `bytearray` objects, and other sets cannot:

```
>>> {"Jane", ["Math", "Physics"]}
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
```

A tuple containing an unhashable value (e.g., a list) also cannot be added to a set.

## Common Set Operations

Most set operations can be performed using an operator or a method.

### Union

```
>>> pet_animals = {"dog", "cat", "hamster", "parrot"}
>>> farm_animals = {"cow", "chicken", "goat", "dog", "cat"}
>>> pet_animals | farm_animals
{'cow', 'hamster', 'cat', 'dog', 'goat', 'chicken', 'parrot'}
>>> pet_animals.union(farm_animals)
{'hamster', 'chicken', 'cow', 'dog', 'parrot', 'cat', 'goat'}
```

Union is commutative. The `|` operator requires both operands to be sets; `.union()` accepts any iterable. Both support multiple sets.

### Intersection

```
>>> john_friends = {"Linda", "Mathew", "Carlos", "Laura"}
>>> jane_friends = {"Alice", "Bob", "Laura", "Mathew"}
>>> john_friends & jane_friends
{'Laura', 'Mathew'}
>>> john_friends.intersection(jane_friends)
{'Laura', 'Mathew'}
>>> a & b & c & d
{4}
```

Intersection returns an empty set when no common elements exist. The operator supports multiple sets; `.intersection()` accepts any number of arguments.

### Difference

```
>>> registered_users = {"Alice", "Bob", "Charlie", "Diana", "Linda"}
>>> checked_in_users = {"Alice", "Charlie", "Linda"}
>>> registered_users - checked_in_users
{'Bob', 'Diana'}
```

Difference is **not** commutative: `checked_in_users - registered_users` yields `set()`. With multiple sets, the operation is performed left to right. `.difference()` accepts any number of arguments.

### Symmetric difference

```
>>> morning_attendees = {"Alice", "Charlie", "Linda", "John", "Jane"}
>>> afternoon_attendees = {"Charlie", "Linda", "Bob", "Jane"}
>>> morning_attendees ^ afternoon_attendees
{'John', 'Bob', 'Alice'}
```

Symmetric difference is commutative (unlike difference). The `^` operator supports multiple sets; `.symmetric_difference()` accepts exactly one argument (chain calls for multiple).

## Augmented Set Operations (In-Place)

Sets support augmented operators that modify the set in place. `frozenset` is immutable and does not support augmented operations.

| Operation | Operator | Method |
|-----------|----------|--------|
| Union | `|=` | `.update()` |
| Intersection | `&=` | `.intersection_update()` |
| Difference | `-=` | `.difference_update()` |
| Symmetric difference | `^=` | `.symmetric_difference_update()` |

Example:

```
>>> checked_in_attendees = set()
>>> checked_in_attendees |= {"Alice", "Charlie"}
>>> checked_in_attendees.update({"Linda", "Bob"})
```

**Note:** Augmented difference uses `-` only on the left side; the optional part uses `|`.

## Comparing Sets

All comparisons return a Boolean rather than a new set.

### Subset / proper subset

```
>>> required_ingredients = {"cheese", "eggs", "milk"}
>>> available_ingredients = {"cheese", "eggs", "milk", "sugar", "salt"}
>>> required_ingredients <= available_ingredients
True
>>> regular_plan < premium_plan   # proper subset
True
>>> a <= a        # a set is a subset of itself
True
>>> a < a         # but not a proper subset of itself
False
```

### Superset / proper superset

```
>>> available_ingredients >= required_ingredients
True
>>> premium_plan > regular_plan   # proper superset
True
>>> a >= a        # a set is a superset of itself
True
>>> a > a         # but not a proper superset of itself
False
```

### Disjoint sets

```
>>> x1.isdisjoint(x2)   # True if no common elements
```

`.isdisjoint()` has no operator equivalent.

## Other Set Methods

| Method | Purpose |
|--------|---------|
| `.add(elem)` | Add a single element (one argument only) |
| `.remove(elem)` | Remove element; raises `KeyError` if missing |
| `.discard(elem)` | Remove element; no error if missing |
| `.pop()` | Remove and return an arbitrary element; raises `KeyError` if empty |
| `.clear()` | Remove all elements |
| `.copy()` | Create a shallow copy |

Sets are implemented like dictionaries with keys but no values, which is why `.remove()` raises `KeyError` for missing elements.

## Traversing Sets

Use `for` loops or `while` loops with `.pop()`. Iteration order is unknown because sets are unordered. To iterate in order, use `sorted()`:

```
>>> for city in sorted(cities):
...     print(city)
```

**Note:** You can’t sort a set in place. `sorted()` returns a new list. You can pass a `key` (e.g., a lambda) to customize sorting.

## Other Capabilities

### `len()`

```
>>> len({"apple", "mango", "orange"})
3
```

`len()` returns the count of distinct items (O(1)).

### Membership tests

```
>>> "Flask" in skills
True
>>> "pandas" in skills
False
```

Sets are hash tables, so membership tests are O(1) on average — much faster than lists (O(n)) for frequent lookups.

## When to Use Sets

Use sets when you need to:

- Store unique items

- Perform many membership tests efficiently

- Eliminate duplicates from an iterable

- Run set operations (union, intersection, difference, symmetric difference)

## See Also

- [Mastering Python Collections](mastering-python-collections.md) — broader treatment of Python collections including lists, tuples, dicts, generators, and comprehensions.
- [Python Tuple](python-tuple.md) — dedicated deep dive on Python’s `tuple` data type (hashable, can be a set element).
