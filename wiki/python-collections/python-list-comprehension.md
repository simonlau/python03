# Python List Comprehension

> Sources: James Timmins (Real Python), 2024-12-07
> Raw: [python-list-comprehension](../../raw/python-collections/python-list-comprehension.md)
> Updated: 2026-10-30

## Overview

List comprehensions in Python provide a concise way to create lists by embedding a loop and optional conditional logic in a single line. You use a list comprehension to transform and filter elements from an iterable efficiently, replacing complex loops and `map()` functions with more readable and often faster expressions.

Key characteristics:

- A list comprehension creates lists by iterating over an iterable and optionally applying a condition.
- List comprehensions can be faster than `for` loops because they’re optimized by Python’s internal mechanisms.
- A list comprehension is **not lazy**—it generates and stores the entire list in memory eagerly.
- Unlike `map()` (which returns an iterable `map` object), a list comprehension returns a list.

## Creating Lists

### With `for` loops

A `for` loop builds a list in three steps: instantiate an empty list, loop over an iterable, and append each element:

```
>>> squares = []
>>> for number in range(10):
...     squares.append(number * number)
...
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### With `map()`

`map()` passes a function and an iterable, returning a `map` object that must be converted to a list:

```
>>> final_prices = map(get_price_with_tax, prices)
>>> list(final_prices)
[1.1772000000000002, 25.4448, ...]
```

### With list comprehensions

A list comprehension defines the list and its contents at once:

```
>>> squares = [number * number for number in range(10)]
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

Format:

```
new_list = [expression for member in iterable]
```

Every list comprehension includes three elements:

1. **`expression`** — the member itself, a method call, or any valid expression returning a value (e.g., `number * number`).

2. **`member`** — the object or value in the iterable (e.g., `number`).

3. **`iterable`** — a list, set, sequence, generator, or any object returning elements one at a time (e.g., `range(10)`).

## Filtering and Conditional Logic

### Filter with `if` at the end

```
>>> sentence = "the rocket came back from mars"
>>> [char for char in sentence if char in "aeiou"]
['e', 'o', 'e', 'a', 'e', 'a', 'o', 'a']
```

### Modify with a conditional expression at the beginning

```
>>> original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
>>> [price if price > 0 else 0 for price in original_prices]
[1.25, 0, 10.22, 3.78, 0, 1.16]
```

Format:

```
new_list = [true_expr if conditional else false_expr for member in iterable]
```

### Set and dictionary comprehensions

Set comprehensions use curly braces and eliminate duplicates:

```
>>> quote = "life, uh, finds a way"
>>> {char for char in quote if char in "aeiou"}
{'a', 'e', 'u', 'i'}
```

Dictionary comprehensions use curly braces with key-value pairs:

```
>>> {number: number * number for number in range(10)}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
```

## Walrus Operator in Comprehensions

Python 3.8 introduced the assignment expression (`:=`), allowing you to run an expression while assigning its output to a variable:

```
>>> [temp for _ in range(20) if (temp := get_weather_data()) >= 100]
[107, 102, 109, 104, 107, 109, 108, 101, 104]
```

The walrus operator needs to be in the conditional part of the comprehension. This creates a coroutine-like pattern where you can access the computed value in both the condition and the expression.

## When Not to Use a List Comprehension

### Nested comprehensions

You can nest comprehensions (e.g., matrices, dictionaries of lists), but nested logic can become confusing:

```
>>> [[number for number in range(5)] for _ in range(6)]
```

Flattening a matrix with a nested comprehension is concise but may be less intuitive than equivalent `for` loops. Prefer clarity over cleverness.

### Large datasets

List comprehensions load the entire output into memory. For very large datasets, use a generator instead:

```
>>> sum(number * number for number in range(1_000_000_000))
333333332833333333500000000
```

Generators evaluate lazily—calculating values only when requested—and keep the memory footprint small. `map()` also operates lazily.

### Performance

Profile different approaches rather than relying on hunches. With `timeit`, comparing `map()`, list comprehensions, and `for` loops across 100 runs showed that `map()` was fastest, the list comprehension was next, and the `for` loop was the slowest — roughly 50 percent slower than `map()`. Choose based on clarity and your specific scenario, then verify with profiling.

## See Also

- [Mastering Python Collections](mastering-python-collections.md) — broader treatment of Python collections including lists, sets, dicts, generators, and comprehensions.
- [Python Generators](python-generators.md) — generator expressions as a lazy alternative to list comprehensions for large datasets.
- [Walrus Operator](../assignment-expressions/walrus-operator.md) — assignment expressions usable inside comprehension conditionals.
- [Command-Line Arguments](../command-line-arguments/command-line-arguments.md) — `sys.argv` lists can be transformed with comprehensions.
