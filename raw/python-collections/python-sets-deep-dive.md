# Sets in Python

> Source: https://realpython.com/python-sets/
> Collected: 2026-10-29
> Published: Unknown

Python provides a built-in `set` data type. It differs from other built-in data types in that it’s an unordered collection of unique elements. It also supports operations that differ from those of other data types.

**By the end of this tutorial, you’ll understand that:**

- A **`set`** is an unordered collection of unique, hashable elements.

- The **`set()` constructor** works by converting any iterable into a set, removing duplicate elements in the process.

- You can **initialize a `set`** using literals, the `set()` constructor, or comprehensions.

- Sets are **unordered** because they don’t maintain a specific order of elements.

- Sets are useful when you need to run **set operations**, **remove duplicates**, run **efficient membership tests**, and more.

## Getting Started With Python’s `set` Data Type

Python’s built-in `set` data type is a mutable and unordered collection of unique and hashable elements. In this definition, the qualifiers mean the following:

- **Mutable**: You can add or remove elements from an existing set.

- **Unordered**: A set doesn’t maintain any particular order of its elements.

- **Unique elements**: Duplicate elements aren’t allowed.

- **Hashable elements**: Each element must have a hash value that stays the same for its entire lifetime.

As with other mutable data types, you can modify sets by increasing or decreasing their size or number of elements. To this end, sets provide a series of handy methods that allow you to add and remove elements to and from an existing set.

The elements of a set must be unique. This feature makes sets especially useful in scenarios where you need to remove duplicate elements from an existing iterable, such as a list or tuple:

```
>>> numbers = [1, 2, 2, 2, 3, 4, 5, 5]
>>> set(numbers)
{1, 2, 3, 4, 5}
```

In practice, removing duplicate items from an iterable might be one of the most useful and commonly used features of sets.

Python implements sets as hash tables. A great feature of hash tables is that they make lookup operations almost instantaneous. Because of this, sets are exceptionally efficient in membership operations with the `in` and `not in` operators.

Finally, Python sets support common set operations, such as union, intersection, difference, symmetric difference, and others. This feature makes them useful when you need to do some of the following tasks:

- Find common elements in two or more sets

- Find differences between two or more sets

- Combine multiple sets together while avoiding duplicates

## Building Sets in Python

To use a set, you first need to create it. You can create sets using set literals, the `set()` constructor, or set comprehensions.

### Creating Sets Through Literals

You can define a new set by providing a comma-separated series of hashable objects within curly braces `{}`:

```
{obj_0[, obj_1, ..., obj_n]}
```

Examples:

```
>>> # Single-element set
>>> hex_colors = {"#33FF57"}
>>> hex_colors
{'#33FF57'}

>>> # Multiple-element set
>>> hex_colors = {
...     "#33FF57",  # Green
...     "#3357FF",  # Blue
...     "#F1C40F",  # Yellow
...     "#E74C3C",  # Red
... }
>>> hex_colors
{'#F1C40F', '#33FF57', '#E74C3C', '#3357FF'}
```

**Note:** You can’t use a literal to create an empty set because an empty pair of curly braces creates a dictionary.

When you define a set following the literal syntax, each object becomes a distinct element. This syntax won’t unpack iterable objects. For example, if you use a tuple, then it’ll be added to the set as a tuple rather than a series of elements:

```
>>> rgb_colors = {
...     (51, 255, 87),  # Green
...     (51, 87, 255),  # Blue
... }
>>> rgb_colors
{(51, 255, 87), (51, 87, 255)}
```

Duplicates are removed:

```
>>> {2, 4, 6, 8, 10, 8, 2}
{2, 4, 6, 8, 10}
>>> {"Smith", "McArthur", "Wilson", "Johansson", "Smith"}
{'Johansson', 'McArthur', 'Wilson', 'Smith'}
```

The elements of a set can be objects of different data types:

```
>>> {42, "Hi!", 3.14159, None, "Python"}
{None, 42, 3.14159, 'Hi!', 'Python'}
```

Set elements must be hashable. You can include a tuple in a set, but you can’t include a list because lists aren’t hashable:

```
>>> rgb_colors = {
...     [51, 255, 87],  # Green
... }
Traceback (most recent call last):
    ...
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
```

Apart from lists, you can’t use dictionaries, `bytearray` objects, or other sets as the elements of a set. These data types are mutable, and therefore, they can’t be hashable.

A special case occurs with tuples. If you have tuples containing hashable values, then you can add those tuples to a set. However, if your tuples contain unhashable values, then you can’t add them to a set:

```
>>> students = {
...     ("Jane", 18, ["Math", "Physics", "History"]),
... }
Traceback (most recent call last):
    ...
TypeError: cannot use 'tuple' as a set element (unhashable type: 'list')
```

### Using the `set()` Constructor

You can also build sets using the `set()` constructor. For example, there’s no literal for creating empty sets because an empty pair of curly braces creates an empty dictionary. If you want to create an empty set, then you have to use the constructor:

```
>>> empty = set()
>>> empty
set()
```

The syntax to build a set using the constructor is:

```
set([iterable])
```

The argument `iterable` is optional and must be an iterable like a list or tuple. For example:

```
>>> set([1, 2, 2, 3, 4, 4, 5])
{1, 2, 3, 4, 5}
```

Python strings are also iterable, so you can pass a string to `set()`. This will generate a set of characters in the input string:

```
>>> language = "Python"
>>> set(language)
{'y', 'P', 'o', 't', 'n', 'h'}
```

The resulting set of characters is unordered. The original order, as specified in the string, isn’t preserved.

There’s a subtle difference between using the `set()` constructor and the literal syntax:

```
>>> set("Hello!")
{'H', 'l', 'e', '!', 'o'}

>>> {"Hello!"}
{'Hello!'}
```

When you create sets using the `set()` constructor, the argument must be iterable. The constructor unpacks the iterable and adds its items to the resulting set as individual elements. In contrast, the set literal syntax adds the iterable as a single element to the set. It doesn’t unpack its items.

### Using Set Comprehensions

A set comprehension is a concise way to create a set by evaluating an expression over an iterable. It works similarly to list comprehensions but automatically removes duplicates.

Here’s the syntax for a set comprehension:

```
{expression for member in iterable [if condition]}
```

A set comprehension returns a new set. So, you use them to create, transform, and filter sets.

To illustrate how to use a set comprehension, say that you have a list of usernames initially entered without validation. You need to clean the list by converting all the usernames to lowercase, removing leading and trailing spaces, and removing duplicates:

```
>>> usernames = [
...     "Alice",
...     " bob",
...     "ALICE  ",
...     "Bob",
...     "charlie",
...     "Charlie",
...     "JOHN"
... ]

>>> {name.lower().strip() for name in usernames}
{'bob', 'alice', 'john', 'charlie'}
```

## Performing Common Set Operations

Python’s `set` data type provides a host of operations based on the operations defined for mathematical sets. You can perform most set operations in two different ways:

1. Using an operator

2. Calling a method

### Union

The union of two sets returns a new set that contains all unique elements from both sets. You can perform a union using the `|` operator or the `.union()` method. Any duplicate elements are automatically removed, so each item appears only once in the result.

Syntax:

```
x1 | x2 [| x3 | ... | xN]
x1.union(x2[, x3, ..., xN])
```

The union operator (`|`) is a binary operator. The `.union()` method can take any number of arguments.

```
>>> pet_animals = {"dog", "cat", "hamster", "parrot"}
>>> farm_animals = {"cow", "chicken", "goat", "dog", "cat"}
>>> pet_animals | farm_animals
{'cow', 'hamster', 'cat', 'dog', 'goat', 'chicken', 'parrot'}
>>> pet_animals.union(farm_animals)
{'hamster', 'chicken', 'cow', 'dog', 'parrot', 'cat', 'goat'}
```

Note that the resulting sets contain only one instance of `"dog"` and `"cat"`. It’s important to mention that the union operation is commutative, meaning the order of the operands doesn’t affect the outcome.

In both examples, the operator and method behave identically. However, there’s a subtle difference between them. When you use the `|` operator, both operands must be sets. The `.union()` method, on the other hand, can take any iterables as arguments:

```
>>> pet_animals | ["cow", "chicken", "goat", "dog", "cat"]
Traceback (most recent call last):
    ...
TypeError: unsupported operand type(s) for |: 'set' and 'list'

>>> pet_animals.union(["cow", "chicken", "goat", "dog", "cat"])
{'hamster', 'chicken', 'cow', 'dog', 'parrot', 'cat', 'goat'}
```

You can use the operator and method with multiple sets:

```
>>> a = {1, 2, 3, 4}
>>> b = {2, 3, 4, 5}
>>> c = {3, 4, 5, 6}
>>> d = {4, 5, 6, 7}
>>> a.union(b, c, d)
{1, 2, 3, 4, 5, 6, 7}
>>> a | b | c | d
{1, 2, 3, 4, 5, 6, 7}
```

### Intersection

The intersection of two sets is a new set containing only the elements common to both sets. You can use the `&` operator or the `.intersection()` method:

```
>>> john_friends = {"Linda", "Mathew", "Carlos", "Laura"}
>>> jane_friends = {"Alice", "Bob", "Laura", "Mathew"}
>>> john_friends & jane_friends
{'Laura', 'Mathew'}
>>> john_friends.intersection(jane_friends)
{'Laura', 'Mathew'}
```

You can specify multiple sets with the intersection operator and method:

```
>>> a = {1, 2, 3, 4}
>>> b = {2, 3, 4, 5}
>>> c = {3, 4, 5, 6}
>>> d = {4, 5, 6, 7}
>>> a & b & c & d
{4}
>>> a.intersection(b, c, d)
{4}
```

If an intersection finds no common elements, you get an empty set:

```
>>> x = {1, 2, 3, 4}
>>> y = {5, 6, 7, 8}
>>> x & y
set()
```

### Difference

The difference between two sets is a new set containing elements that are in the first set but not in the second. You can perform a difference using the `-` operator or the `.difference()` method:

```
>>> registered_users = {"Alice", "Bob", "Charlie", "Diana", "Linda"}
>>> checked_in_users = {"Alice", "Charlie", "Linda"}
>>> registered_users - checked_in_users
{'Bob', 'Diana'}
```

Note that in the case of set difference, the order of the operands affects the result:

```
>>> checked_in_users - registered_users
set()
```

Now, you get an empty set, which demonstrates that the difference operation isn’t commutative.

You can specify more than two sets:

```
>>> a = {1, 2, 3, 30, 300}
>>> b = {10, 20, 30, 40}
>>> c = {100, 200, 300, 400}
>>> a - b - c
{1, 2, 3}
>>> a.difference(b, c)
{1, 2, 3}
```

When you specify multiple sets, the operation is performed from left to right.

### Symmetric Difference

The symmetric difference between two sets is a new set containing all the elements that appear in either set but not both. You can perform a symmetric difference using the `^` operator or the `.symmetric_difference()` method:

```
>>> morning_attendees = {"Alice", "Charlie", "Linda", "John", "Jane"}
>>> afternoon_attendees = {"Charlie", "Linda", "Bob", "Jane"}
>>> morning_attendees ^ afternoon_attendees
{'John', 'Bob', 'Alice'}
>>> morning_attendees.symmetric_difference(afternoon_attendees)
{'John', 'Bob', 'Alice'}
```

Note that unlike the set difference operation, symmetric difference is commutative:

```
>>> afternoon_attendees ^ morning_attendees
{'John', 'Bob', 'Alice'}
```

The symmetric difference operator (`^`) also allows you to process more than two sets:

```
>>> a = {1, 2, 3, 4, 5}
>>> b = {10, 2, 3, 4, 50}
>>> c = {1, 50, 100}
>>> a ^ b ^ c
{100, 5, 10}
```

Curiously, the `.symmetric_difference()` method doesn’t support multiple arguments:

```
>>> a.symmetric_difference(b, c)
Traceback (most recent call last):
    ...
TypeError: set.symmetric_difference() takes exactly one argument (2 given)
```

You can work around this behavior by chaining calls:

```
>>> a.symmetric_difference(b).symmetric_difference(c)
{10, 100, 5}
```

## Using Augmented Set Operations

The union, intersection, difference, and symmetric difference operators covered in the previous section have augmented variations that you can use to modify a set in place. Remember, sets are mutable data types, so you can add and remove elements from a set in place.

**Note:** Python has a variation of sets called `frozenset` that’s immutable. This built-in data type works like normal sets but doesn’t allow you to add or remove elements. Additionally, they don’t support augmented operations.

For each augmented operator, you’ll have an equivalent method.

### Augmented Union

The augmented union updates a set in place. You can use either the augmented union operator (`|=`) or the `.update()` method:

```
>>> checked_in_attendees = set()
>>> checked_in_attendees |= {"Alice", "Charlie"}
>>> checked_in_attendees
{'Charlie', 'Alice'}
>>> checked_in_attendees.update({"Linda", "Bob"})
>>> checked_in_attendees
{'Charlie', 'Bob', 'Linda', 'Alice'}
```

### Augmented Intersection

The intersection update allows you to modify a set in place by intersection. You can perform this operation using the augmented intersection operator (`&=`) or the `.intersection_update()` method:

```
>>> accepted_emails = {"Bob", "Diana", "Charlie"}
>>> target_customers = {"Alice", "Bob", "Charlie", "Diana", "Jane"}
>>> target_customers &= accepted_emails
>>> target_customers
{'Charlie', 'Bob', 'Diana'}
```

### Augmented Difference

The difference update lets you modify a set in place by difference. You can run this type of update using the augmented difference operator (`-=`) or the `.difference_update()` method:

```
>>> todo_list = {
...     "Implement user login",
...     "Fix bug #123",
...     "Improve performance",
...     "Write unit tests"
... }
>>> completed_tasks = {
...     "Fix bug #123",
...     "Improve performance"
... }
>>> todo_list.difference_update(completed_tasks)
>>> todo_list
{'Implement user login', 'Write unit tests'}
```

**Note:** The syntax for the augmented difference operator differs from the syntax of augmented union and augmented intersection. Note that the minus sign (`-`) isn’t used in the optional part of the syntax. Instead, you have to use the union operator (`|`).

### Augmented Symmetric Difference

The symmetric difference update allows you to modify a set by symmetric difference. You can perform this operation with the augmented symmetric difference operator (`^=`) or the `.symmetric_difference_update()` method:

```
>>> morning_attendees = {"Alice", "Charlie", "Linda", "John", "Jane"}
>>> afternoon_attendees = {"Charlie", "Linda", "Bob", "Jane"}
>>> whole_day_attendees = set()
>>> whole_day_attendees ^= morning_attendees
>>> whole_day_attendees.symmetric_difference_update(afternoon_attendees)
>>> whole_day_attendees
{'Bob', 'Alice', 'John'}
```

## Comparing Sets

You can also use operators and methods to compare two sets. In the context of sets, relational operators like `>`, `<`, `>=`, and `<=` have a slightly different interpretation than in numerical comparisons. All the checks return a Boolean value rather than a new set.

### Subsets

The subset operation lets you determine whether one set is contained in another. You can use the `<=` operator or the `.issubset()` method:

```
>>> required_ingredients = {"cheese", "eggs", "milk"}
>>> available_ingredients = {"cheese", "eggs", "milk", "sugar", "salt"}
>>> required_ingredients <= available_ingredients
True
>>> required_ingredients.issubset(available_ingredients)
True
```

A set `x1` is a subset of another set `x2` if every element of `x1` is in `x2`. A set is considered a subset of itself:

```
>>> a = {1, 2, 3, 4, 5}
>>> a <= a
True
>>> a.issubset(a)
True
```

### Proper Subsets

With this check, you can determine whether one set is a proper subset of another. You’ll use the `<` operator. You won’t have a dedicated method:

```
>>> regular_plan = {"Tutorials", "Quizzes"}
>>> premium_plan = {"Tutorials", "Video Courses", "Quizzes", "Books"}
>>> regular_plan < premium_plan
True
```

A proper subset is a subset with the additional requirement that the compared sets can’t be identical. While a set is considered a subset of itself, it isn’t a proper subset of itself:

```
>>> a = {1, 2, 3, 4, 5}
>>> a < a
False
```

### Supersets

The superset check lets you determine whether one set contains another. You can use the `>=` operator or the `.issuperset()` method:

```
>>> available_ingredients >= required_ingredients
True
>>> available_ingredients.issuperset(required_ingredients)
True
```

A superset is the opposite of a subset. A set is also considered a superset of itself:

```
>>> a = {1, 2, 3, 4, 5}
>>> a.issuperset(a)
True
>>> a >= a
True
```

### Proper Supersets

With this check, you can determine whether one set is a proper superset of another. You’ll use the `>` operator. As with a proper subset, you won’t have a dedicated method:

```
>>> premium_plan > regular_plan
True
```

A proper superset is also a superset, except that the involved sets can’t be identical. A set isn’t a proper superset of itself:

```
>>> a > a
False
```

### Disjoint Sets

Finally, you have the disjoint check, which allows you to determine if two sets don’t have any elements in common. In this case, you only have a dedicated method called `.isdisjoint()`. You won’t have an operator:

```
>>> x1.isdisjoint(x2)
```

The `x1.isdisjoint(x2)` call returns `True` if `x1` and `x2` have no elements in common.

```
>>> def verify_purchase(age, selection, restricted_products):
...     if age < 21 and not selection.isdisjoint(restricted_products):
...         print("Purchase denied: selection includes age-restricted products")
...     else:
...         print("Purchase approved")
...
>>> verify_purchase(
...     age=18,
...     selection={"milk", "bread", "beer"},
...     restricted_products={"alcohol", "beer", "cigarettes"}
... )
Purchase denied: selection includes age-restricted products
```

## Using Other Set Methods

So far, you’ve learned about set-specific operations. There are a mix of methods that you can call on sets to change their content. You’ll find methods for adding elements to a set and also for removing elements from a set.

### Adding an Element With `.add()`

The `.add()` method allows you to add a single element to an existing set:

```
>>> employees = {"Alice", "Charlie"}
>>> employees.add("John")
>>> employees
{'Charlie', 'John', 'Alice'}
```

Note that when you call `.add()` with an element that’s already in the set, nothing happens. Finally, you can only pass one argument to `.add()`. Otherwise, you get a `TypeError` exception:

```
>>> employees.add("Jane", "Bob")
Traceback (most recent call last):
    ...
TypeError: set.add() takes exactly one argument (2 given)
```

### Removing an Existing Element With `.remove()`

If you need to remove elements from a set, then use the `.remove()` method. You can call this method with the element you want to remove. However, keep in mind that you’ll get an exception if the target element isn’t found in the set:

```
>>> employees = {"Alice", "Charlie", "John", "Laura"}
>>> employees.remove("Charlie")
>>> employees
{'John', 'Laura', 'Alice'}
>>> employees.remove("Linda")
Traceback (most recent call last):
    ...
KeyError: 'Linda'
```

With `.remove()`, you can delete one element at a time. When the target element doesn’t exist in the set, you get a `KeyError` exception. Why a `KeyError`? Well, sets are implemented like dictionaries with keys but without associated values. So, set elements are like dictionary keys.

### Deleting an Existing or Missing Element With `.discard()`

Like `.remove()`, the `.discard()` method allows you to remove a single element from an existing set. The difference between both methods is that `.discard()` doesn’t raise an exception if the element doesn’t exist:

```
>>> employees = {"Alice", "Charlie", "John", "Laura"}
>>> employees.discard("Alice")
>>> employees
{'Charlie', 'John', 'Laura'}
>>> employees.discard("Linda")
>>> employees
{'Charlie', 'John', 'Laura'}
```

### Removing and Returning an Element With `.pop()`

Sometimes, you need to retrieve an element from a set, process it, and then remove it. In that case, you can use the `.pop()` method, which removes and returns an element from a set. If the target set is empty, then `.pop()` raises a `KeyError` exception:

```
>>> employees = {"Alice", "Charlie", "John", "Laura"}
>>> employee = employees.pop()
>>> employee
'Charlie'
```

The `.pop()` method removes and returns an arbitrary element from a set in one go. Because sets are unordered data types, you can’t predict which element will be removed.

### Removing All Elements With `.clear()`

If you ever need to remove all the elements from a set in a single operation, then you can use the `.clear()` method:

```
>>> employees = {"Alice", "Charlie", "John", "Laura"}
>>> employees.clear()
>>> employees
set()
```

### Creating Shallow Copies of Sets With `.copy()`

You can use the `.copy()` method to create a shallow copy of an existing set:

```
>>> employees = {"Alice", "Charlie", "John", "Laura"}
>>> employees_copy = employees.copy()
>>> employees == employees_copy
True
>>> employees is employees_copy
False
>>> employees.remove("Alice")
>>> employees
{'Charlie', 'John', 'Laura'}
>>> employees_copy  # Keeps the data unchanged
{'Charlie', 'Alice', 'John', 'Laura'}
```

## Traversing Sets

When working with Python sets, you’ll often need to traverse their elements in order to perform actions on them. A Python `for` loop lets you do that. If you want to iterate over a set while processing and removing its elements, then you can use a `while` loop.

However, you need to keep in mind that in both situations, the iteration order will be unknown beforehand because sets are unordered data types. If you need to examine a set’s content in order, then you can loop through it using the built-in `sorted()` function.

### Accessing and Modifying Elements in a Loop

Python sets are mutable in the sense that you can add or remove elements from them. However, you can’t modify a set element in place as you can with list items:

```
>>> employees = {"Alice", "Charlie", "John", "Laura"}
>>> for employee in employees:
...     print(f"Hello, {employee}!")
...
Hello, Charlie!
Hello, John!
Hello, Laura!
Hello, Alice!
```

If you want to modify the elements of a set, then you should create a new set:

```
>>> employees = {"Alice", "Charlie", "John", "Laura"}
>>> uppercase = set()
>>> for employee in employees:
...     uppercase.add(employee.upper())
...
>>> uppercase
{'ALICE', 'CHARLIE', 'JOHN', 'LAURA'}
```

You can achieve the same result using a set comprehension:

```
>>> {employee.upper() for employee in employees}
{'ALICE', 'CHARLIE', 'JOHN', 'LAURA'}
```

### Processing and Removing Elements in a Loop

The `.pop()` method comes in handy when you need to process throwaway elements before removing them:

```
>>> available_seats = {"A1", "A2", "B1", "B2", "C1"}
>>> while available_seats:
...     assigned_seat = available_seats.pop()
...     print(f"Seat {assigned_seat} was assigned")
...
Seat B1 was assigned
Seat A1 was assigned
Seat B2 was assigned
Seat C1 was assigned
Seat A2 was assigned
>>> available_seats
set()
```

### Iterating Through a Sorted Set

As you already know, sets don’t keep their elements in order. Therefore, you can’t predict which element will be processed in each iteration. The built-in `sorted()` function can help you put some order to your iteration:

```
>>> cities = {"Vancouver", "Berlin", "London", "Warsaw", "Vienna"}
>>> for city in sorted(cities):
...     print(city)
...
Berlin
London
Vancouver
Vienna
Warsaw
```

**Note:** You can’t sort a set in place because they’re unordered data types. With the `sorted()` function, you get a new list containing the set’s elements in sorted order. This list takes additional memory.

You can sort by a custom key using a lambda function:

```
>>> cities = {
...     ("Vancouver", 675000),
...     ("Berlin", 3800000),
...     ("London", 8980000),
...     ("Warsaw", 1790000),
...     ("Vienna", 1900000),
... }
>>> for city in sorted(cities, key=lambda city: city[1]):
...     print(city)
...
('Vancouver', 675000)
('Warsaw', 1790000)
('Vienna', 1900000)
('Berlin', 3800000)
('London', 8980000)
```

## Exploring Other Set Capabilities

Python sets work seamlessly with some built-in functions and operators. Among the most popular are the `len()` function and the membership operators `in` and `not in`, which provide efficient ways to work with sets.

### Finding the Number of Elements With `len()`

To find out how many elements a set contains, simply call the `len()` function with your set as an argument:

```
>>> fruits = {"apple", "mango", "orange"}
>>> len(fruits)
3
```

Because sets don’t allow duplicates, you’ll always get the count of distinct items, making `len()` a quick way to verify the uniqueness of your data.

### Running Membership Tests on Sets

You can use the Python `in` and `not in` operators to check whether an element belongs to a collection or container. These checks are known as membership tests and can be pretty useful in real-world coding.

Because Python sets are implemented as hash tables, it turns out that they’re very efficient for membership tests, especially compared to `list` objects. So, when you need to perform frequent membership tests on a collection, you’ll benefit from using a set.

## Conclusion

You’ve learned a lot about Python’s `set` data type, which is an unordered collection of unique and hashable elements. You’ve explored different ways to create sets, including using literals, the `set()` constructor, and set comprehensions.

Additionally, you’ve learned about common set operations such as union, intersection, difference, and symmetric difference, as well as several set manipulation techniques.

Understanding sets can make a difference in your Python journey. Sets provide efficient ways to handle collections of unique items, perform membership tests, and execute set operations. They come in handy when you need to eliminate duplicates or perform fast lookups.

**In this tutorial, you’ve learned how to:**

- Create sets using literals, the `set()` constructor, and comprehensions

- Perform common set operations such as union, intersection, difference, and symmetric difference

- Use augmented set operations to modify sets in place

- Compare sets using subset, superset, and disjoint checks

- Manipulate sets by adding, removing, and traversing their elements

With these skills, you can now effectively use Python sets to manage collections of unique items, optimize your code for performance, and solve problems involving set theory and operations. This knowledge will enable you to write more efficient and clean Python code.

## Frequently Asked Questions

**What is a `set` in Python and how does it differ from a list?**

A `set` in Python is an unordered collection of unique and hashable elements, unlike a list, which is ordered and can contain duplicate elements.

**How do you create a `set` in Python?**

You can create a `set` using literals that consist of a pair of curly braces `{}` with a comma-separated series of elements inside, or by using the `set()` constructor or a set comprehension.

**What are some common set operations you can perform on Python’s `set`?**

You can perform operations like union, intersection, difference, and symmetric difference on Python sets.

**How can you add or remove elements from a `set` in Python?**

You can add elements to a `set` using the `.add()` method and remove elements with the `.remove()`, `.discard()`, or `.pop()` methods.

**What are some scenarios where using a `set` is beneficial?**

Using a `set` is beneficial when you need to store unique items, perform many membership tests, or eliminate duplicates from an iterable.
