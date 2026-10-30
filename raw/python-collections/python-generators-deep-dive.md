# How to Use Generators and yield in Python

> Source: https://realpython.com/introduction-to-python-generators/
> Collected: 2026-10-30
> Published: Unknown

Have you ever had to work with a dataset so large that it overwhelmed your machine’s memory? Or maybe you have a complex function that needs to maintain an internal state every time it’s called, but the function is too small to justify creating its own class. In these cases and more, generators and the Python yield statement are here to help.

**By the end of this article, you’ll know:**

- What **generators** are and how to use them

- How to create **generator functions and expressions**

- How the **Python yield** statement works

- How to use **multiple** Python yield statements in a generator function

- How to use **advanced generator methods**

- How to **build data pipelines** with multiple generators

## Using Generators

Introduced with PEP 255, **generator functions** are a special kind of function that return a lazy iterator. These are objects that you can loop over like a list. However, unlike lists, lazy iterators do not store their contents in memory.

### Example 1: Reading Large Files

A common use case of generators is to work with data streams or large files, like CSV files. Now, what if you want to count the number of rows in a CSV file?

The naive approach loads everything into memory at once:

```
def csv_reader(file_name):
    file = open(file_name)
    result = file.read().split("\n")
    return result
```

If the file is larger than available memory, this raises `MemoryError`. The generator-based version opens the file and yields each row instead of returning a list:

```
def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row
```

This version opens a file, loops through each line, and yields each row instead of returning it. It can process very large files without memory errors:

```
Row count is 64186394
```

Key difference:

- Using `yield` results in a generator object.

- Using `return` results in the first line of the file *only*.

You can also define a **generator expression** (also called a generator comprehension), which has a very similar syntax to list comprehensions:

```
csv_gen = (row for row in open(file_name))
```

### Example 2: Generating an Infinite Sequence

Generating an infinite sequence requires the use of a generator, since computer memory is finite:

```
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
```

This code initializes `num`, starts an infinite loop, yields `num`, then increments it. Using `next()` on the generator object manually iterates over it:

```
>>> gen = infinite_sequence()
>>> next(gen)
0
>>> next(gen)
1
>>> next(gen)
2
```

**Note:** When you use `next()`, Python calls `.__next__()` on the iterator. In practice, you’re unlikely to write your own infinite sequence generator. The `itertools` module provides `itertools.count()`.

### Example 3: Detecting Palindromes

A practical use for infinite sequences is building palindrome detectors — locating sequences of letters or numbers that read the same forward and backward, like 121.

```
def is_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0
    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10
    return num == reversed_num
```

Use your infinite sequence generator to get a running list of all numeric palindromes:

```
>>> for i in infinite_sequence():
...     pal = is_palindrome(i)
...     if pal:
...         print(i)
...
11
22
33
[...]
```

## Understanding Generators

Generator functions look and act just like regular functions, but with one defining characteristic: they use the Python `yield` keyword instead of `return`. `yield` indicates where a value is sent back to the caller, but unlike `return`, you don’t exit the function afterward. Instead, the **state** of the function is remembered. When `next()` is called on a generator object, the previously yielded variable is incremented and yielded again.

### Building Generators With Generator Expressions

Like list comprehensions, generator expressions allow you to quickly create a generator object:

```
>>> nums_squared_lc = [num**2 for num in range(5)]
>>> nums_squared_gc = (num**2 for num in range(5))
```

The first uses brackets to build a list; the second uses parentheses to create a generator object:

```
>>> nums_squared_lc
[0, 1, 4, 9, 16]
>>> nums_squared_gc
<generator object <genexpr> at 0x107fbbc78>
```

### Profiling Generator Performance

Generators optimize memory. A list comprehension of 10,000 squared numbers is 85,176 bytes, while the generator object is only 208 bytes — over 400 times smaller.

```
>>> import sys
>>> nums_squared_lc = [i ** 2 for i in range(10000)]
>>> sys.getsizeof(nums_squared_lc)
85176
>>> nums_squared_gc = (i ** 2 for i in range(10000))
>>> print(sys.getsizeof(nums_squared_gc))
208
```

However, list comprehensions can be faster to evaluate than generator expressions when speed is an issue and memory isn’t.

## Understanding the Python Yield Statement

`yield` controls the flow of a generator function in a way similar to `return` statements. When you call `next()` on a generator, the code within the function executes up to `yield`. When the `yield` statement is hit, the program suspends function execution and returns the yielded value to the caller. (In contrast, `return` stops function execution completely.) When a function is suspended, the state of that function is saved — including variable bindings, instruction pointer, internal stack, and exception handling. This allows you to resume function execution whenever you call one of the generator’s methods.

### Multiple yield statements

You can use multiple `yield` statements in a generator function:

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
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

Unless your generator is infinite, you can iterate through it one time only. Once all values have been evaluated, iteration stops and `StopIteration` is raised.

## Using Advanced Generator Methods

Generator objects can use the following methods:

- `.send()`

- `.throw()`

- `.close()`

### How to Use `.send()`

As of Python 2.5, `yield` is an **expression**, rather than just a statement. This allows you to use `yield` as:

```
i = (yield num)
```

This lets `.send()` send a value back to the generator. When execution picks up after `yield`, `i` takes the value that is sent.

Example — an infinite palindrome generator that skips ahead after each palindrome:

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

This creates a **coroutine** — a generator function into which you can pass data.

### How to Use `.throw()`

`.throw()` allows you to throw exceptions into the generator:

```
>>> pal_gen.throw(ValueError("We don't like large palindromes"))
ValueError: We don't like large palindromes
```

`.throw()` is useful where you need to catch exceptions. You can stop iteration more elegantly with `.close()`.

### How to Use `.close()`

`.close()` stops a generator by raising `GeneratorExit` inside it:

```
>>> pal_gen.close()
```

The `.send()` call after `.close()` raises `StopIteration`.

## Creating Data Pipelines With Generators

Data pipelines let you string together code to process large datasets or streams without maxing out memory. Example: analyzing a large CSV file (TechCrunch Continental USA set) to get the total and average of all series A rounds.

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

This script pulls together every generator into one big data pipeline. Running it on `techcrunch.csv` finds a total of $4,380,015,000 raised in series A funding rounds.

**Note:** For robust CSV parsing, use the `csv` module from Python’s standard library instead of manual string splitting.

## Conclusion

In this tutorial, you learned about generator functions and generator expressions:

- How to use and write generator functions and generator expressions

- How the Python yield statement enables generators

- How to use multiple yield statements in a generator function

- How to use `.send()` to send data to a generator

- How to use `.throw()` to raise generator exceptions

- How to use `.close()` to stop a generator’s iteration

- How to build a generator pipeline to efficiently process large CSV files
