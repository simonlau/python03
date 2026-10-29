# Python's tuple Data Type: A Deep Dive With Examples

> Source: https://realpython.com/python-tuple/
> Collected: 2026-10-29
> Published: Unknown

In Python, a **`tuple`** is a built-in data type that allows you to create **immutable sequences** of values. The values or items in a tuple can be of any type. This makes tuples pretty useful in those situations where you need to store heterogeneous data, like that in a database record, for example.

Through this tutorial, you’ll dive deep into Python tuples and get a solid understanding of their key features and use cases. This knowledge will allow you to write more efficient and reliable code by taking advantage of tuples.

**In this tutorial, you’ll learn how to:**

- **Create** tuples in Python

- **Access** the items in an existing tuple

- **Unpack**, **return**, **copy**, and **concatenate** tuples

- **Reverse**, **sort**, and **traverse** existing tuples

- Explore other **features** and common **gotchas** of tuples

In addition, you’ll explore some alternative tools that you can use to replace tuples and make your code more readable and explicit.

To get the most out of this tutorial, you should have a good understanding of a few Python concepts, including variables, functions, and `for` loops. Familiarity with other built-in data structures, especially lists, is also a plus.

## Getting Started With Python’s `tuple` Data Type

The built-in `tuple` data type is probably the most elementary sequence available in Python. Tuples are immutable and can store a fixed number of items. For example, you can use tuples to represent Cartesian coordinates `(x, y)`, RGB colors `(red, green, blue)`, records in a database table `(name, age, job)`, and many other sequences of values.

In all these use cases, the number of elements in the underlying tuple is *fixed*, and the items are *unchangeable*.

Some of the most relevant characteristics of `tuple` objects include the following:

- **Ordered**: They contain elements that are sequentially arranged according to their specific insertion order.

- **Lightweight**: They consume relatively small amounts of memory compared to other sequences like lists.

- **Indexable through a zero-based index**: They allow you to access their elements by integer indices that start from zero.

- **Immutable**: They don’t support in-place mutations or changes to their contained elements. They don’t support growing or shrinking operations.

- **Heterogeneous**: They can store objects of different data types and domains, including mutable objects.

- **Nestable**: They can contain other tuples, so you can have tuples of tuples.

- **Iterable**: They support iteration, so you can traverse them using a loop or comprehension while you perform operations with each of their elements.

- **Sliceable**: They support slicing operations, meaning that you can extract a series of elements from a tuple.

- **Combinable**: They support concatenation operations, so you can combine two or more tuples using the concatenation operators, which creates a new tuple.

- **Hashable**: They can work as keys in dictionaries when all the tuple items are immutable.

Tuples are sequences of objects. They’re commonly called **containers** or **collections** because a single tuple can contain or collect an arbitrary number of other objects.

## Constructing Tuples in Python

A tuple is a sequence of comma-separated objects. To store objects in a tuple, you need to create the tuple object with all its content at one time. You can create tuples using tuple literals or the `tuple()` constructor.

### Creating Tuples Through Literals

Tuple literals consist of a comma-separated series of objects. The general syntax:

```
item_0, item_1, ..., item_n
```

The commas are required; the parentheses are optional in most cases but improve readability:

```
(item_0, item_1, ..., item_n)
```

Examples:

```
>>> jane = ("Jane Doe", 25, 1.75, "Canada")
>>> point = (2, 7)
>>> pen = (2, "Solid", True)
```

In the case of `days`, you should note that Python ignores any extra comma at the end of a tuple, as it happens after `"Sunday"`. So, it’s optional but common practice because it allows you to quickly add a new item if needed.

**Empty tuple:** The parentheses *are* required when creating an empty tuple:

```
>>> empty = ()
>>> type(empty)
<class 'tuple'>
```

Once created, you can’t populate an empty tuple with new data as you can do with lists, because tuples are immutable.

**Single-item tuple:** To create a tuple with a single item, you need to place the item followed by a comma. The comma is the only required part of the syntax:

```
>>> one_word = "Hello",
>>> one_word
('Hello',)

>>> one_number = (42,)
>>> one_number
(42,)
```

The trailing comma is required. Single-item tuples are useful, for example, as the value of the `.__slots__` special attribute in a class with only one instance attribute.

### Using the `tuple()` Constructor

You can also use the `tuple()` class constructor to create tuple objects from an iterable, such as a list, set, dictionary, or string:

```
tuple([iterable])
```

Examples:

```
>>> tuple(["Jane Doe", 25, 1.75, "Canada"])
('Jane Doe', 25, 1.75, 'Canada')

>>> tuple("Pythonista")
('P', 'y', 't', 'h', 'o', 'n', 'i', 's', 't', 'a')

>>> tuple({
...     "manufacturer": "Boeing",
...     "model": "747",
...     "passengers": 416,
... }.values())
('Boeing', '747', 416)

>>> tuple()
()
```

The `tuple()` constructor also accepts sets, but remember that sets are unordered, which will affect the final order of items in the resulting tuple. Calling `tuple()` without an argument returns a new empty tuple.

The `tuple()` constructor comes in handy when you need to create a tuple out of an iterator object. The constructor will consume the iterator, build a tuple from its data, and return it:

```
>>> tuple(x**2 for x in range(10))
(0, 1, 4, 9, 16, 25, 36, 49, 64, 81)
```

Potentially infinite iterators will hang your code if you feed them to the `tuple()` constructor.

## Accessing Items in a Tuple: Indexing

You can extract the items of a tuple using their associated indices. Indices start at `0` and go up to the number of items in the tuple minus `1`:

```
tuple_object[index]
```

Examples:

```
>>> jane = ("Jane Doe", 25, 1.75, "Canada")
>>> jane[0]
'Jane Doe'
>>> jane[1]
25
>>> jane[3]
'Canada'
```

Indexing is an *O(1)* operation, so tuples are good for situations where you need to quickly access specific items from a series.

If you use an index greater than or equal to the tuple’s length, you get an `IndexError`:

```
>>> jane[4]
Traceback (most recent call last):
    ...
IndexError: tuple index out of range
```

You can also use negative indices, which give you access to tuple items in backward order:

```
>>> jane[-1]
'Canada'
>>> jane[-2]
1.75
```

A negative index specifies an element’s position relative to the right end of the tuple. The index `-1` accesses the last item, `-2` the item next to the last, and so forth. If you use an index lower than `-len(tuple_object)`, you get an `IndexError`.

When you have a tuple that contains other sequences, you can access items in nested sequences by chaining indexing operations:

```
>>> employee = (
...     "John",
...     35,
...     "Python Developer",
...     ("Django", "Flask", "FastAPI", "CSS", "HTML"),
... )
>>> employee[-1][0]
'Django'
```

## Retrieving Multiple Items From a Tuple: Slicing

Like other Python sequences, tuples allow you to extract a slice of their content:

```
tuple_object[start:stop:step]
```

| Index | Description | Default Value |
|-------|-------------|---------------|
| `start` | Index at which to start slicing (included) | `0` |
| `stop` | Index at which to stop slicing (not included) | `len(tuple_object)` |
| `step` | How many items to jump through on each step | `1` |

Examples:

```
>>> days = (
...     "Monday", "Tuesday", "Wednesday", "Thursday",
...     "Friday", "Saturday", "Sunday",
... )
>>> days[:5]
('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
>>> days[5:]
('Saturday', 'Sunday')
```

For deeper slicing details, see the list slicing section. The same slicing operations that apply to lists are valid for tuples, except for those that mutate a list in place.

## Exploring Tuple Immutability

Python’s tuples are immutable, which means that once created, you can’t change or update their items in place:

```
>>> jane = ("Jane Doe", 25, 1.75, "Canada")
>>> jane[3] = "United States"
Traceback (most recent call last):
    ...
TypeError: 'tuple' object does not support item assignment
```

Tuples don’t support growing or shrinking either. Unlike lists, tuples don’t have `.append()`, `.extend()`, `.insert()`, `.remove()`, or `.clear()` methods. Tuples also don’t support the `del` statement on items.

Even though tuples are immutable, they can store mutable objects. You can change the content of mutable objects even if they’re nested in a tuple:

```
>>> student_info = ("Linda", 18, ["Math", "Physics", "History"])
>>> student_info[2][2] = "Computer science"
>>> student_info
('Linda', 22, ['Math', 'Physics', 'Computer science'])
```

Because tuples are immutable, you can use them as keys in a dictionary — but only if all their items are hashable:

```
>>> student_courses = {
...     ("John", "Doe"): ["Physics", "Chemistry"],
...     ("Jane", "Doe"): ["English", "History"],
... }
>>> student_courses[("Jane", "Doe")]
['English', 'History']
```

If the tuple contains mutable objects, you’ll get a `TypeError: unhashable type: 'list'`.

## Packing and Unpacking Tuples

When you write `point = x, y, z`, you’re *packing* the values of `x`, `y`, and `z` in `point`. You can also *unpack* the values of a tuple into variables:

```
>>> point = (7, 14, 21)
>>> x, y, z = point
>>> x
7
>>> y
14
>>> z
21
```

In regular unpacking, the number of variables must match the number of values, otherwise you get a `ValueError`.

A popular use case is swapping values between variables without a temporary variable:

```
>>> a = 200
>>> b = 400
>>> a, b = b, a
>>> a
400
>>> b
200
```

Python also has a packing/unpacking operator (`*`) to collect multiple values in a single variable:

```
>>> numbers = (1, 2, 3, 4, 5)
>>> *head, last = numbers
>>> head
[1, 2, 3, 4]
>>> last
5

>>> first, *middle, last = numbers
>>> first
1
>>> middle
[2, 3, 4]
>>> last
5
```

Note that the `*` operator collects values in a new `list`, not a tuple. You can also use `*` to merge tuples:

```
>>> name = ("John", "Doe")
>>> contact = ("john@example.com", "55-555-5555")
>>> (*name, *contact)
('John', 'Doe', 'john@example.com', '55-555-5555')
```

## Returning Tuples From Functions

To return multiple values from a function, build a `return` statement with a comma-separated series of arguments — that’s a tuple:

```
>>> def find_extremes(iterable):
...     data = tuple(iterable)
...     if len(data) == 0:
...         raise ValueError("input iterable must not be empty")
...     return min(data), max(data)
...
>>> extremes = find_extremes([3, 4, 2, 6, 7, 1, 9])
>>> extremes
(1, 9)
```

The built-in `divmod()` function is a good example — it returns a tuple containing the quotient and remainder:

```
>>> divmod(4, 2)
(2, 0)
>>> quotient, remainder = divmod(8, 2)
```

If your function needs several different return types, you’re dealing with a more complex scenario; type hints can help.

## Creating Copies of a Tuple

Because tuples are immutable, creating copies isn’t really necessary. Shallow copying techniques (slicing operator or `copy.copy()`) create aliases instead of copies:

```
>>> student_info = ("Linda", 18, ["Math", "Physics", "History"])
>>> student_profile = student_info[:]
>>> id(student_info) == id(student_profile)
True
```

The `copy()` function from the `copy` module produces the same result — both variables hold references to the same tuple object.

If the tuple hosts a mutable object (like a list), changes to that object affect both aliases:

```
>>> student_profile[2][2] = "Computer science"
>>> student_profile
('Linda', 18, ['Math', 'Physics', 'Computer science'])
>>> student_info
('Linda', 18, ['Math', 'Physics', 'Computer science'])
```

For deep copies, use `deepcopy()`:

```
>>> from copy import deepcopy
>>> student_profile = deepcopy(student_info)
>>> id(student_info) == id(student_profile)
False
```

`deepcopy()` creates a new tuple object; changes to mutable objects in the copy won’t affect the original.

## Concatenating and Repeating Tuples

Tuples support concatenation with the plus operator (`+`) and repetition with the star operator (`*`):

```
>>> personal_info = ("John", 35)
>>> professional_info = ("Computer science", ("Python", "Django", "Flask"))
>>> profile = personal_info + professional_info
>>> profile
('John', 35, 'Computer science', ('Python', 'Django', 'Flask'))
```

You can only concatenate a tuple with another tuple; concatenating with a list raises `TypeError`.

The augmented concatenation operator (`+=`) works similarly — it creates a new tuple every time because tuples are immutable:

```
>>> profile = ("John", 35)
>>> profile += ("Computer science", ("Python", "Django", "Flask"))
```

Repetition clones the content of a tuple a specific number of times:

```
>>> numbers = (1, 2, 3)
>>> numbers * 3
(1, 2, 3, 1, 2, 3, 1, 2, 3)
>>> 4 * numbers
(1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)
```

The order of operands doesn’t affect repetition. The augmented repetition operator (`*=`) always creates a new tuple object.

## Reversing and Sorting Tuples

Python provides `reversed()` and `sorted()` functions, and you can reverse tuples with slicing using a step of `-1`:

```
>>> tuple(reversed(days))
('Sunday', 'Saturday', 'Friday', ...)

>>> reversed_days = days[::-1]
```

`reversed()` returns an iterator; you need `tuple()` to consume it. Slicing with `[::-1]` creates a new reversed tuple directly.

`sorted()` returns a **list** of sorted values, not a tuple:

```
>>> numbers = (2, 9, 5, 1, 6)
>>> sorted(numbers)
[1, 2, 5, 6, 9]
>>> sorted(numbers, reverse=True)
[9, 6, 5, 2, 1]
```

Sorting tuples with heterogeneous data may raise `TypeError` because items can’t be compared:

```
>>> sorted(("John Doe", 35, "Python Developer"))
Traceback (most recent call last):
    ...
TypeError: '<' not supported between instances of 'int' and 'str'
```

The `key` argument allows fine-tuning:

```
>>> fruits = (("apple", 0.40), ("banana", 0.25), ("orange", 0.35))
>>> sorted(fruits, key=lambda fruit: fruit[1])
[('banana', 0.25), ('orange', 0.35), ('apple', 0.4)]
```

## Traversing Tuples in Python

You can traverse tuples using `for` loops, comprehensions, generator expressions, `map()`, and `filter()`.

### Using a `for` Loop

```
>>> monthly_incomes = (
...     ("January", 5000), ("February", 5500), ...,
...     ("December", 5500)
... )
>>> total_income = 0
>>> for income in monthly_incomes:
...     total_income += income[1]
>>> total_income
75100
```

You can use tuple unpacking in the header of a `for` loop, combined with `enumerate()`:

```
>>> for index, (month, income) in enumerate(monthly_incomes, start=1):
...     print(f"{month:>10}: {income}")
```

### Using a Comprehension or Generator Expression

```
>>> numbers = ("2", "9", "5", "1", "6")
>>> tuple([int(number) for number in numbers])
(2, 9, 5, 1, 6)
>>> tuple(int(number) for number in numbers)
(2, 9, 5, 1, 6)
```

A generator expression is more memory-efficient than a comprehension.

## Exploring Other Features of Tuples

Tuples have only two methods in their public API: `.count()` and `.index()`.

```
>>> fruits = ("apple", "banana", "orange", "apple", "apple", "kiwi", "banana")
>>> fruits.count("apple")
3
>>> fruits.index("apple")
0
>>> fruits.index("mango")
Traceback (most recent call last):
    ...
ValueError: tuple.index(x): x not in tuple
```

Membership tests with `in`/`not in`:

```
>>> skills = ("Python", "Django", "Flask", "CSS")
>>> "Flask" in skills
True
>>> "pandas" in skills
False
```

Membership operations on tuples have O(n) time complexity. For frequent membership tests, consider sets (O(1) lookup).

### Getting the Length

```
>>> len(employee)
4
```

Calling `len()` on a tuple is O(1) because tuples track their length internally.

### Comparing Tuples

Tuples support standard comparison operators using lexicographical ordering — item-by-item comparison:

```
>>> (2, 3) == (2, 3)
True
>>> (5, 6, 7) < (7, 5, 6)
True
>>> (4, 3, 2) <= (4, 3, 2)
True
```

Comparing tuples with heterogeneous types using `<` or `>` may raise `TypeError` if items can’t be compared.

## Common Gotchas of Python Tuples

**One-item tuple without trailing comma:** Parentheses alone don’t create a tuple; the comma does:

```
>>> numbers = (42)
>>> type(numbers)
<class 'int'>
>>> numbers = (42,)
>>> type(numbers)
<class 'tuple'>
```

**Hashability:** Tuples are usable as dictionary keys only if all items are hashable. Tuples containing lists are unhashable and raise `TypeError`.

## Using Alternatives to the Built-in `tuple` Type

Tuples have limited functionality — you can only access items using numeric indices, which can be error-prone. Python offers alternatives with named fields:

### `collections.namedtuple`

A named tuple is a tuple subclass with named fields, accessible via dot notation:

```
>>> from collections import namedtuple
>>> Person = namedtuple("Person", "name age position")
>>> person = Person("John", 35, "Python Developer")
>>> person.name
'John'
>>> person[0]
'John'
```

Named tuples are immutable. A cool use case is wrapping `divmod()`:

```
>>> DivMod = namedtuple("DivMod", "quotient remainder")
>>> def custom_divmod(a, b):
...     return DivMod(*divmod(a, b))
>>> custom_divmod(8, 4)
DivMod(quotient=2, remainder=0)
```

### `typing.NamedTuple`

A typed version of `namedtuple` with type hints and default values:

```
>>> from typing import NamedTuple
>>> class Employee(NamedTuple):
...     name: str
...     age: int
...     position: str = "Python Developer"
```

### Data Classes: `dataclasses.dataclass`

Python 3.7 added data classes, similar to named tuples but mutable by default:

```
>>> from dataclasses import dataclass
>>> @dataclass
... class Employee:
...     name: str
...     age: int
...     position: str = "Python Developer"
```

Pass `frozen=True` to make a data class immutable:

```
>>> @dataclass(frozen=True)
... class Employee:
...     name: str
...     age: int
...     position: str = "Python Developer"
```

## Deciding Whether to Use Tuples

Use tuples when you need to:

- **Ensure data integrity**: Immutability guarantees values remain unchanged.
- **Reduce memory consumption**: Tuples have less memory overhead than lists.
- **Improve performance**: Tuples are generally more efficient than lists for creation, iteration, and element access.

Concrete use cases:

- Associating two or more values (pairs, trios)
- Representing database records
- Providing multi-value keys in dictionaries

Examples:

```
>>> color = (0, 2, 255)
>>> car = ("Toyota", "Camry", 2020, "Blue")
>>> capital_cities = {
...    ("Ottawa", (45.4215, -75.6972)): "Canada",
...    ("Washington D.C.", (38.9072, -77.0369)): "USA",
...    ("Berlin", (52.5200, 13.4050)): "Germany",
... }
```

## Conclusion

Tuples are immutable sequences that provide a reliable container for data likely to remain unmodified during your code’s lifetime. You’ve learned how to create tuples, access items via indexing and slicing, unpack/return/copy/concatenate tuples, reverse/sort/traverse tuples, and explore alternatives like `namedtuple`, `typing.NamedTuple`, and data classes.
