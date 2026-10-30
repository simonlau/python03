# Python Generators

> Sources: Kyle Stratis (Real Python), 2026-10-26
> Raw: [python-generators-deep-dive](../../raw/python-collections/python-generators-deep-dive.md)
> Updated: 2026-10-30

## Overview

Python’s **generators** are a special kind of function that return a lazy iterator — objects you can loop over like a list, but unlike lists, they do not store their contents in memory. Introduced with PEP 255, generators and the Python `yield` statement help when working with datasets so large they would overwhelm your machine’s memory, or when a function needs to maintain internal state between calls without justifying a full class.

## Creating Generators

### Generator functions

Generator functions look and act like regular functions but use `yield` instead of `return`:

```
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
```

`yield` sends a value back to the caller but does not exit the function. The function’s state is remembered, so when `next()` is called again, execution resumes right after `yield`:

```
>>> gen = infinite_sequence()
>>> next(gen)
0
>>> next(gen)
1
>>> next(gen)
2
```

### Generator expressions

Generator expressions have a syntax similar to list comprehensions but use parentheses:

```
>>> nums_squared_lc = [num**2 for num in range(5)]
>>> nums_squared_gc = (num**2 for num in range(5))
>>> nums_squared_lc
[0, 1, 4, 9, 16]
>>> nums_squared_gc
<generator object <genexpr> at 0x107fbbc78>
```

### Key difference: `yield` vs `return`

Using `yield` results in a generator object; using `return` results in only the first value.

```
def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row
```

This generator-based file reader yields one row at a time instead of loading the entire file into memory, avoiding `MemoryError` on very large files.

## Performance

Generators optimize memory:

```
>>> import sys
>>> nums_squared_lc = [i ** 2 for i in range(10000)]
>>> sys.getsizeof(nums_squared_lc)
85176
>>> nums_squared_gc = (i ** 2 for i in range(10000))
>>> print(sys.getsizeof(nums_squared_gc))
208
```

A list of 10,000 squared numbers is 85,176 bytes; the generator object is only 208 bytes — over 400 times smaller. However, list comprehensions can be faster to evaluate when memory isn’t a concern and speed is.

## The `yield` Statement

`yield` controls the flow of a generator function. When `next()` is called, code executes up to `yield`, then suspends and returns the yielded value. The function’s state (local variables, instruction pointer, stack, exception handling) is saved so execution can resume after `yield`.

### Multiple `yield` statements

```
>>> def multi_yield():
...     yield_str = "This will print the first string"
...     yield yield_str
...     yield_str = "This will print the second string"
...     yield yield_str
...
>>> multi_obj = multi_yield()
>>> print(next(multi_obj))
This will print the first string
>>> print(next(multi_obj))
This will print the second string
>>> print(next(multi_obj))
StopIteration
```

Unless a generator is infinite, it can be iterated only once. Once exhausted, `StopIteration` is raised (the natural exception signaling the end of an iterator; `for` loops are built around it).

## Advanced Generator Methods

### `.send()`

As of Python 2.5, `yield` is an expression, not just a statement:

```
i = (yield num)
```

This lets `.send()` pass data back into the generator. When execution resumes after `yield`, `i` takes the sent value. If `next()` or a `for` loop is used, `i` is `None`.

Example — an infinite palindrome generator that skips ahead after each palindrome (a coroutine):

```
def infinite_palindromes():
    num = 0
    while True:
        if is_palindrome(num):
            i = (yield num)
            if i is not None:
                num = i
        num += 1

pal_gen = infinite_palindromes()
for i in pal_gen:
    digits = len(str(i))
    pal_gen.send(10 ** (digits))
```

### `.throw()`

`.throw()` raises an exception inside the generator:

```
>>> pal_gen.throw(ValueError("We don't like large palindromes"))
ValueError: We don't like large palindromes
```

Useful for controlling iteration via exceptions, though `.close()` is more elegant for stopping.

### `.close()`

`.close()` stops a generator by raising `GeneratorExit` inside it:

```
>>> pal_gen.close()
```

A `.send()` call after `.close()` raises `StopIteration`.

## Data Pipelines

Generators let you string together code to process large datasets without maxing out memory. Example: analyzing a large CSV file (TechCrunch Continental USA set) for total series A funding:

```
file_name = "techcrunch.csv"
lines = (line for line in open(file_name))
list_line = (s.rstrip().split(",") for s in lines)
cols = next(list_line)
company_dicts = (dict(zip(cols, data)) for data in list_line)
funding = (
    int(company_dict["raisedAmt"])
    for company_dict in company_dicts
    if company_dict["round"] == "a"
)
total_series_a = sum(funding)
print(f"Total series A fundraising: ${total_series_a}")
```

Each generator expression chains into the next, forming one big data pipeline. Iteration only happens when `sum()` is called. Running on `techcrunch.csv` yields $4,380,015,000 in series A funding.

**Note:** For robust CSV parsing, use Python’s standard-library `csv` module instead of manual string splitting.

## See Also

- [Mastering Python Collections](mastering-python-collections.md) — broader treatment of Python collections including lists, tuples, sets, dicts, generators, and comprehensions.
- [Python Tuple](python-tuple.md) — tuples are hashable and can be used in generator-based pipelines.
- [Python Set](python-set.md) — sets support efficient membership tests for filtering in generator pipelines.
- [Command-Line Arguments](../command-line-arguments/command-line-arguments.md) — generator pipelines can process data from command-line file arguments.
