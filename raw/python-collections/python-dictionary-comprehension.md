# Python Dictionary Comprehensions: How and When to Use Them

> Source: https://realpython.com/python-dictionary-comprehension/
> Collected: 2026-10-30
> Published: Unknown

Dictionary comprehensions are a concise and quick way to create, transform, and filter dictionaries in Python. They can significantly enhance your code’s conciseness and readability compared to using regular `for` loops to process your dictionaries.

Understanding dictionary comprehensions is crucial for you as a Python developer because they’re a Pythonic tool for dictionary manipulation and can be a valuable addition to your programming toolkit.

**In this tutorial, you’ll learn how to:**

- **Create** dictionaries using dictionary comprehensions

- **Transform** existing dictionaries with comprehensions

- **Filter** key-value pairs from dictionaries using conditionals

- **Decide** when to use dictionary comprehensions

To get the most out of this tutorial, you should be familiar with basic Python concepts, such as `for` loops, iterables, and dictionaries, as well as list comprehensions.

## Creating and Transforming Dictionaries in Python

In Python programming, you’ll often need to create, populate, and transform dictionaries. To do this, you can use dictionary literals, the `dict()` constructor, and `for` loops. You’ll also learn about dictionary comprehensions, which are a powerful way to manipulate dictionaries in Python.

### Creating Dictionaries With Literals and `dict()`

To create new dictionaries, you can use literals. A dictionary literal is a series of key-value pairs enclosed in curly braces:

```
{key_1: value_1, key_2: value_2,..., key_N: value_N}
```

The keys must be hashable objects and are commonly strings. The values can be any Python object, including other dictionaries:

```
>>> likes = {"color": "blue", "fruit": "apple", "pet": "dog"}
>>> likes
{'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}

>>> likes["hobby"] = "guitar"
>>> likes
{'color': 'blue', 'fruit': 'apple', 'pet': 'dog', 'hobby': 'guitar'}
```

You can also create new dictionaries using the `dict()` constructor:

```
>>> dict(apple=0.40, orange=0.35, banana=0.25)
{'apple': 0.4, 'orange': 0.35, 'banana': 0.25}
```

The `dict()` constructor is only suitable for cases where the dictionary keys can be strings that are valid Python identifiers.

### Using `for` Loops to Populate Dictionaries

Sometimes, you need to start with an empty dictionary and populate it with key-value pairs dynamically. For example, say that you want to create a dictionary in which keys are integer numbers and values are powers of `2`:

```
>>> powers_of_two = {}

>>> for integer in range(1, 10):
...     powers_of_two[integer] = 2**integer
...

>>> powers_of_two
{1: 2, 2: 4, 3: 8, 4: 16, 5: 32, 6: 64, 7: 128, 8: 256, 9: 512}
```

### Introducing Dictionary Comprehensions

Dictionary comprehensions allow you to build dictionaries with a one-line `for` loop. The main difference from list comprehensions is that dictionary comprehensions use curly braces instead of square brackets. Additionally, the comprehension expression must include a key and a value separated by a colon.

Here’s the syntax for a dictionary comprehension:

```
{key: value for member in iterable [if condition]}
```

A dictionary comprehension returns a new dictionary. To build this dictionary, you compute the key-value pairs from the items of an input iterable. Note that the syntax includes an optional conditional at the end, which you can use to filter existing dictionaries.

The comprehension syntax includes four elements:

1. **Enclosing brackets:** Curly braces (`{}`) are used for dictionary comprehensions.

2. **The comprehension expression:** An expression that provides a value in each iteration. In dictionary comprehension, the expression must provide the key and its corresponding value, `key: value`. Both elements can be expressions.

3. **The current `member`:** This is the current item or value in the iterable.

4. **The `iterable`:** This can be any Python iterable object, including a list, tuple, set, generator, or similar.

The following code shows how you can build the `power_of_two` dictionary using a comprehension:

```
>>> power_of_two = {integer: 2**integer for integer in range(1, 10)}

>>> power_of_two
{1: 2, 2: 4, 3: 8, 4: 16, 5: 32, 6: 64, 7: 128, 8: 256, 9: 512}
```

In this example, `integer: 2**integer` is the comprehension expression, `integer` is the current member, and `range(1, 10)` is the iterable.

Comprehensions can also have more than one `for` clause. When they do, the leftmost `for` iterates over the outer collection, the next `for` from left to right iterates over the first nesting level, and so on:

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

In this example, the first `for` loop iterates over the rows of your matrix. The second `for` loop iterates over the number of each row. As a result, you get a dictionary that maps numbers to their square values. Even though this syntax works, it can make your comprehensions difficult to read and understand.

It’s important to note that in this example, instead of having 16 key-value pairs, you end up with only nine. This is because dictionary keys are unique. When the key is duplicated, the new value overrides the previous one.

## Leveraging Dictionary Comprehensions in Python

With dictionary comprehensions, you can create new dictionaries, transform existing ones, and even filter key-value pairs.

### Creating Dictionaries From Iterables

Sometimes, you have an iterable of data and want to create a dictionary by using the data items to generate the keys and values, while also applying some transformation to the original data:

```
>>> fruits = ["apple", "banana", "cherry"]

>>> {fruit.upper(): len(fruit) for fruit in fruits}
{'APPLE': 5, 'BANANA': 6, 'CHERRY': 6}
```

In this example, you apply transformations to generate the keys and values.

Consider the following example that creates a dictionary with lowercase letters as keys and their Unicode code points as values:

```
>>> from string import ascii_lowercase

>>> {letter: ord(letter) for letter in ascii_lowercase}
{
    'a': 97,
    'b': 98,
    'c': 99,
    'd': 100,
    'e': 101,
    ...
    'z': 122,
}
```

Sometimes, you have two data sequences and want to map each item in the first sequence to the corresponding item in the second. In this case, you can use the `zip()` function:

```
>>> parts = [
...     "CPU",
...     "GPU",
...     "Motherboard",
...     "RAM",
...     "SSD",
...     "Power Supply",
...     "Case",
...     "Cooling Fan"
... ]

>>> stocks = [15, 8, 12, 30, 25, 10, 5, 20]

>>> {part: stock for part, stock in zip(parts, stocks)}
{
    'CPU': 15,
    'GPU': 8,
    'Motherboard': 12,
    'RAM': 30,
    'SSD': 25,
    'Power Supply': 10,
    'Case': 5,
    'Cooling Fan': 20
}
```

In practice, when you need to create a dictionary from two sequences without applying any transformation on the data items, you can use `dict(zip(parts, stocks))` instead of a comprehension. However, if you need to transform the data somehow, then you’d benefit from using a comprehension:

```
>>> part_costs = [250, 500, 150, 80, 100, 120, 70, 25]

>>> {
...     part: stock * cost
...     for part, stock, cost in zip(parts, stocks, part_costs)
... }
{
    'CPU': 3750,
    'GPU': 4000,
    'Motherboard': 1800,
    'RAM': 2400,
    'SSD': 2500,
    'Power Supply': 1200,
    'Case': 350,
    'Cooling Fan': 500,
}
```

### Transforming Existing Dictionaries

You can also use comprehensions to transform the keys or values of existing dictionaries. A typical example is when you need to swap keys and values:

```
>>> parts = {
...     "CPU": 10021,
...     "GPU": 10022,
...     "Motherboard": 10023,
...     "RAM": 10024,
...     "SSD": 10025,
...     "Power Supply": 10027,
...     "Case": 10026,
...     "Cooling Fan": 10025,
... }

>>> {value: key for key, value in parts.items()}
{
    10021: 'CPU',
    10022: 'GPU',
    10023: 'Motherboard',
    10024: 'RAM',
    10025: 'Cooling Fan',
    10027: 'Power Supply',
    10026: 'Case'
}
```

To swap the keys and values of a dictionary, you need to have values that are hashable objects. Also, the values must be unique, or you’ll end up losing part of the data corresponding to the duplicate values.

You can get the same result using `dict(zip(parts.values(), parts.keys()))`.

As another example, say that you have a dictionary of fruits and their prices, and you need to decrease the prices by 5%:

```
>>> fruits = {
...     "apple": 1.00,
...     "banana": 0.50,
...     "cherry": 2.00,
... }

>>> {fruit: round(price * 0.95, 2) for fruit, price in fruits.items()}
{'apple': 0.95, 'banana': 0.48, 'cherry': 1.90}
```

### Filtering Items From Dictionaries

Dictionary comprehensions also allow you to use a conditional at the end of their syntax. This conditional will enable you to create dictionaries by filtering existing data:

```
>>> numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}

>>> {key: value for key, value in numbers.items() if value % 2 == 0}
{'two': 2, 'four': 4}
```

The conditional at the end of the comprehension filters odd numbers from the original dictionary. As a result, you get a dictionary of even numbers.

To filter a dictionary by keys:

```
>>> codes = {
...     "1001": "Townsville",
...     "1002": "Lakeview",
...     "1003": "Mountainview",
...     "1101": "Riverside",
...     "1102": "Hilltop",
...     "1201": "Greenfield",
...     "1202": "Sunnydale",
...     "1301": "Meadowbrook",
...     "1302": "Creekwood"
... }

>>> {code: town for code, town in codes.items() if "1100" <= code <= "1300"}
{
    '1101': 'Riverside',
    '1102': 'Hilltop',
    '1201': 'Greenfield',
    '1202': 'Sunnydale'
}
```

## Deciding When to Use Dictionary Comprehensions

When deciding whether to use a dictionary comprehension instead of regular loops or a combination of function calls, you should consider the following factors:

- **Conciseness**: Dictionary comprehensions reduce the amount of code compared to equivalent `for` loops.

- **Readability**: Dictionary comprehensions can make your code more explicit and readable.

In practice, you can use dictionary comprehensions when you need to do some of the following operations:

- Create a dictionary from an existing iterable

- Merge iterables into a dictionary while transforming keys, values, or both

- Transform dictionary keys, values, or both

- Filter an existing dictionary

Finally, there are situations when you want to avoid dictionary comprehensions. For example, when you want to process a large dataset to produce key-value pairs. Using dictionary comprehension in this situation will create a large dictionary and store it in memory, which will result in high memory consumption.

To make your code memory-efficient, you may use a generator expression that yields tuples of the form `(key, value)` instead:

```
>>> squares_generator = ((x, x * x) for x in range(1_000_000))
>>> squares_generator
<generator object <genexpr> at 0x106e2ac20>

>>> next(squares_generator)
(0, 0)
>>> next(squares_generator)
(1, 1)
>>> next(squares_generator)
(2, 4)
>>> next(squares_generator)
(3, 9)
```

The resulting iterator yields tuples on demand, meaning that you’ll only use memory to store one tuple at a time. You don’t need to store a dictionary of a million key-value pairs in your computer’s memory, and avoiding this will make your code more efficient.

Instead, you can use the built-in `next()` function to traverse the resulting iterator, or you can use a `for` loop.

**Note:** You don’t get direct look-up with a generator. If you rely on looking up the values by their key, then a generator expression is a clumsy replacement for a dictionary comprehension.

## Exploring Common Bad Practices

You should avoid a few bad practices when working with dictionary comprehensions in your Python code:

- Using **complex expressions** in comprehensions

- Writing **nested comprehensions** with several `for` clauses or several conditionals

- Running **costly transformations** while building the keys and values

- Trying to **access comprehension variables** from the outside

```
>>> {value: value**3 for value in range(1, 11)}
{
    1: 1,
    2: 8,
    3: 27,
    4: 64,
    5: 125,
    6: 216,
    7: 343,
    8: 512,
    9: 729,
    10: 1000
}

>>> value
Traceback (most recent call last):
    ...
NameError: name 'value' is not defined
```

The `value` variable is only visible within the comprehension. If you try to use it outside the comprehension, then you get a `NameError`.

## Conclusion

You’ve learned about Python dictionary comprehensions in detail. They’re a powerful tool for creating, transforming, and filtering dictionaries using concise and clean syntax.

**In this tutorial, you’ve:**

- **Created** new dictionaries with a concise syntax

- **Transformed** existing dictionaries with comprehensions

- **Filtered** unwanted key-value pairs from dictionaries

- **Decided** when to use comprehensions in your code
