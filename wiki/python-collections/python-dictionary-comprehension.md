# Python Dictionary Comprehension

> Sources: Leodanis Pozo Ramos (Real Python), 2024-11-13
> Raw: [python-dictionary-comprehension](../../raw/python-collections/python-dictionary-comprehension.md)
> Updated: 2026-10-30

## Overview

Dictionary comprehensions are a concise and quick way to create, transform, and filter dictionaries in Python. They can significantly enhance your code’s conciseness and readability compared to using regular `for` loops to process your dictionaries. Dictionary comprehensions are a Pythonic tool for dictionary manipulation.

## Creating Dictionaries

### Dictionary literals and `dict()`

A dictionary literal is a series of key-value pairs enclosed in curly braces:

```
{key_1: value_1, key_2: value_2,..., key_N: value_N}
```

The keys must be hashable objects and are commonly strings. The values can be any Python object:

```
>>> likes = {"color": "blue", "fruit": "apple", "pet": "dog"}
>>> likes["hobby"] = "guitar"
```

You can also use the `dict()` constructor, but only when the keys are strings that are valid Python identifiers:

```
>>> dict(apple=0.40, orange=0.35, banana=0.25)
{'apple': 0.4, 'orange': 0.35, 'banana': 0.25}
```

### Dictionary comprehension syntax

The syntax uses curly braces and requires a `key: value` pair in the expression:

```
{key: value for member in iterable [if condition]}
```

The comprehension syntax includes four elements:

1. **Enclosing brackets:** Curly braces (`{}`).

2. **The comprehension expression:** Must provide the key and its corresponding value, `key: value`. Both elements can be expressions.

3. **The current `member`:** The current item or value in the iterable.

4. **The `iterable`:** Any Python iterable (list, tuple, set, generator, etc.).

Example — powers of two:

```
>>> power_of_two = {integer: 2**integer for integer in range(1, 10)}
>>> power_of_two
{1: 2, 2: 4, 3: 8, 4: 16, 5: 32, 6: 64, 7: 128, 8: 256, 9: 512}
```

Multiple `for` clauses are supported. The leftmost `for` iterates over the outer collection:

```
>>> matrix = [
...     [9, 3, 8, 3],
...     [4, 5, 2, 8],
...     [6, 4, 3, 1],
...     [1, 0, 4, 5],
... ]
>>> {value: value**2 for row in matrix for value in row}
{9: 81, 3: 9, 8: 64, 4: 16, 5: 25, 2: 4, 6: 36, 1: 1, 0: 0}
```

Note: dictionary keys are unique. When a key is duplicated, the new value overrides the previous one — so the example above yields only nine pairs instead of sixteen.

## Creating Dictionaries From Iterables

You can transform items from an iterable into keys and values:

```
>>> fruits = ["apple", "banana", "cherry"]
>>> {fruit.upper(): len(fruit) for fruit in fruits}
{'APPLE': 5, 'BANANA': 6, 'CHERRY': 6}
```

Map two sequences using `zip()`:

```
>>> parts = ["CPU", "GPU", "Motherboard", "RAM"]
>>> stocks = [15, 8, 12, 30]
>>> {part: stock for part, stock in zip(parts, stocks)}
{'CPU': 15, 'GPU': 8, 'Motherboard': 12, 'RAM': 30}
```

Without transformations, `dict(zip(parts, stocks))` is more Pythonic than a comprehension. Use a comprehension when you need to compute the values:

```
>>> part_costs = [250, 500, 150, 80]
>>> {part: stock * cost for part, stock, cost in zip(parts, stocks, part_costs)}
{'CPU': 3750, 'GPU': 4000, 'Motherboard': 1800, 'RAM': 2400}
```

## Transforming Existing Dictionaries

Use `.items()` to transform keys, values, or both:

```
>>> parts = {
...     "CPU": 10021,
...     "GPU": 10022,
...     "Motherboard": 10023,
...     "RAM": 10024,
... }
>>> {value: key for key, value in parts.items()}
{10021: 'CPU', 10022: 'GPU', 10023: 'Motherboard', 10024: 'RAM'}
```

To swap keys and values, the values must be hashable and unique — otherwise duplicate values cause data loss.

Transform values (decrease prices by 5%):

```
>>> fruits = {"apple": 1.00, "banana": 0.50, "cherry": 2.00}
>>> {fruit: round(price * 0.95, 2) for fruit, price in fruits.items()}
{'apple': 0.95, 'banana': 0.48, 'cherry': 1.90}
```

## Filtering Items From Dictionaries

Use a conditional at the end of the comprehension:

```
>>> numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
>>> {key: value for key, value in numbers.items() if value % 2 == 0}
{'two': 2, 'four': 4}
```

Filter by keys:

```
>>> codes = {"1001": "Townsville", "1002": "Lakeview", "1101": "Riverside", "1102": "Hilltop"}
>>> {code: town for code, town in codes.items() if "1100" <= code <= "1300"}
{'1101': 'Riverside', '1102': 'Hilltop'}
```

## When to Use Dictionary Comprehensions

Use dictionary comprehensions when you need to:

- Create a dictionary from an existing iterable
- Merge iterables into a dictionary while transforming keys, values, or both
- Transform dictionary keys, values, or both
- Filter an existing dictionary

Avoid them when:

- Processing a very large dataset (a comprehension creates the whole dictionary in memory)
- The expression is too complex (hurts readability)
- You need nested comprehensions with several `for` clauses or conditionals
- You need to run costly transformations while building keys and values

For large datasets, prefer a generator expression yielding `(key, value)` tuples:

```
>>> squares_generator = ((x, x * x) for x in range(1_000_000))
>>> next(squares_generator)
(0, 0)
```

Note: a generator doesn’t support direct key lookup — if you need lookups by key, a generator is a clumsy replacement for a dictionary comprehension.

## Common Bad Practices

- Using complex expressions in comprehensions
- Writing nested comprehensions with several `for` clauses or conditionals
- Running costly transformations while building keys and values
- Trying to access comprehension variables from the outside (raises `NameError`)

```
>>> {value: value**3 for value in range(1, 11)}
{1: 1, 2: 8, 3: 27, ..., 10: 1000}
>>> value
NameError: name 'value' is not defined
```

## See Also

- [Mastering Python Collections](mastering-python-collections.md) — broader treatment of Python collections including dictionaries.
- [Python List Comprehension](python-list-comprehension.md) — list comprehensions share similar syntax with dictionary comprehensions.
- [Python Set](python-set.md) — set comprehensions share similar syntax with dictionary comprehensions.
- [Python Generators](python-generators.md) — generator expressions as a memory-efficient alternative for large datasets.
