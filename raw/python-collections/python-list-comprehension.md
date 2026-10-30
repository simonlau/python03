# Python List Comprehension: Tutorial With Examples

> Source: https://realpython.com/list-comprehension-python/
> Collected: 2026-10-30
> Published: Unknown

List comprehensions in Python provide a concise way to create lists by embedding a loop and optional conditional logic in a single line. You use a list comprehension to transform and filter elements from an iterable efficiently. It allows you to replace complex loops and `map()` functions with more readable and often faster expressions. By understanding list comprehensions, you can optimize your code for better performance and clarity.

**By the end of this tutorial, you’ll understand that:**

- A **list comprehension** in Python is a tool for creating lists by iterating over an iterable and optionally applying a condition.

- You should use **list comprehensions** instead of loops when you want concise, readable code that performs transformations or filtering.

- You add **conditional logic** to a list comprehension by including an `if` statement within the comprehension.

- A **list comprehension** can be faster than a `for` loop because it’s optimized for performance by Python’s internal mechanisms.

- A **Python list comprehension** is not lazy—it generates and stores the entire list in memory eagerly.

- The difference between **list comprehensions** and `map()` is that the former creates a list, while the latter returns a `map` object, which is iterable.

## Transforming Lists in Python

There are a few different ways to create and add items to a list in Python. You can use `for` loops and the `map()` function to perform these tasks, then move on to list comprehensions.

### Use `for` Loops

The most common type of loop is the `for` loop. You can use a `for` loop to create a list of elements in three steps:

1. Instantiate an empty list.
2. Loop over an iterable or `range` of elements.
3. Append each element to the end of the list.

If you want to create a list containing the first ten perfect squares:

```
>>> squares = []
>>> for number in range(10):
...     squares.append(number * number)
...
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### Work With `map` Objects

For an alternative approach based in functional programming, you can use `map()`. You pass in a function and an iterable, and `map()` will create an object. This object contains the result you’d get from running each iterable element through the supplied function.

```
>>> prices = [1.09, 23.56, 57.84, 4.56, 6.78]
>>> TAX_RATE = .08
>>> def get_price_with_tax(price):
...     return price * (1 + TAX_RATE)
...

>>> final_prices = map(get_price_with_tax, prices)
>>> final_prices
<map object at 0x7f34da341f90>

>>> list(final_prices)
[1.1772000000000002, 25.4448, 62.467200000000005, 4.9248, 7.322400000000001]
```

You pass both arguments to `map()` and store the resulting `map` object, then convert it into a list using `list()`.

### Leverage List Comprehensions

List comprehensions are a third way of making or transforming lists. You could rewrite the `for` loop from the first example in just a single line of code:

```
>>> squares = [number * number for number in range(10)]
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

Rather than creating an empty list and adding each element to the end, you define the list and its contents at the same time by following this format:

```
new_list = [expression for member in iterable]
```

Every list comprehension includes three elements:

1. **`expression`** is the member itself, a call to a method, or any other valid expression that returns a value. In the example above, `number * number` is the square of the member value.

2. **`member`** is the object or value in the list or iterable. In the example above, the member value is `number`.

3. **`iterable`** is a list, set, sequence, generator, or any other object that can return its elements one at a time. In the example above, the iterable is `range(10)`.

Because the expression requirement is so flexible, a list comprehension works well in many places where you would use `map()`. You can rewrite the pricing example with its own list comprehension:

```
>>> final_prices = [get_price_with_tax(price) for price in prices]
>>> final_prices
[1.1772000000000002, 25.4448, 62.467200000000005, 4.9248, 7.322400000000001]
```

The only distinction between this implementation and `map()` is that the list comprehension returns a list, not a map object.

## Supercharging Your Python List Comprehensions

List comprehensions can be used for mapping and filtering.

### Filter Values From a List

The most common way to add conditional logic to a list comprehension is to add a conditional to the end of the expression:

```
new_list = [expression for member in iterable if conditional]
```

Conditionals allow list comprehensions to filter out unwanted values, which would normally require a call to `filter()`:

```
>>> sentence = "the rocket came back from mars"
>>> [char for char in sentence if char in "aeiou"]
['e', 'o', 'e', 'a', 'e', 'a', 'o', 'a']
```

The conditional can test any valid expression. For a more complex filter, move the conditional logic to a separate function:

```
>>> sentence = (
...     "The rocket, who was named Ted, came back "
...     "from Mars because he missed his friends."
... )
>>> def is_consonant(letter):
...     vowels = "aeiou"
...     return letter.isalpha() and letter.lower() not in vowels
...

>>> [char for char in sentence if is_consonant(char)]
['T', 'h', 'r', 'c', 'k', 't', ...]
```

You can place the conditional at the end for basic filtering, but what if you want to change a member value instead of filtering it out? Place the conditional near the beginning by taking advantage of the conditional expression:

```
new_list = [true_expr if conditional else false_expr for member in iterable]
```

For example, replace negative prices with 0 and leave positive values unchanged:

```
>>> original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
>>> [price if price > 0 else 0 for price in original_prices]
[1.25, 0, 10.22, 3.78, 0, 1.16]
```

### Remove Duplicates With Set and Dictionary Comprehensions

While list comprehensions are common, you can also create set and dictionary comprehensions. A set comprehension is almost exactly the same as a list comprehension, but set comprehensions make sure the output contains no duplicates:

```
>>> quote = "life, uh, finds a way"
>>> {char for char in quote if char in "aeiou"}
{'a', 'e', 'u', 'i'}
```

Dictionary comprehensions are similar, with the additional requirement of defining a key:

```
>>> {number: number * number for number in range(10)}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
```

### Assign Values With the Walrus Operator

Python 3.8 introduced the assignment expression, also known as the walrus operator (`:=`). It allows you to run an expression while simultaneously assigning the output value to a variable:

```
>>> import random
>>> def get_weather_data():
...     return random.randrange(90, 110)
...

>>> [temp for _ in range(20) if (temp := get_weather_data()) >= 100]
[107, 102, 109, 104, 107, 109, 108, 101, 104]
```

Note that the walrus operator needs to be in the conditional part of your comprehension. You won’t often need to use the assignment expression inside a list comprehension, but it’s a useful tool to have at your disposal when necessary.

## Deciding When Not to Use a List Comprehension

List comprehensions are useful but they’re not the right choice for all circumstances. They might make your code run more slowly or use more memory. If your code is less performant or harder to understand, then it’s probably better to choose an alternative.

### Watch Out for Nested Comprehensions

You can nest comprehensions to create combinations of lists, dictionaries, and sets within a collection. For example:

```
>>> cities = ["Austin", "Tacoma", "Topeka", "Sacramento", "Charlotte"]
>>> {city: [0 for _ in range(7)] for city in cities}
```

Nested lists are a common way to create matrices:

```
>>> [[number for number in range(5)] for _ in range(6)]
[
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4]
]
```

Flattening a matrix with a nested list comprehension is concise but may not be intuitive:

```
>>> matrix = [
...     [0, 0, 0],
...     [1, 1, 1],
...     [2, 2, 2],
... ]

>>> [number for row in matrix for number in row]
[0, 0, 0, 1, 1, 1, 2, 2, 2]
```

Using `for` loops to flatten the same matrix is more straightforward:

```
>>> flat = []
>>> for row in matrix:
...     for number in row:
...         flat.append(number)
...
>>> flat
[0, 0, 0, 1, 1, 1, 2, 2, 2]
```

### Choose Generators for Large Datasets

A list comprehension loads the entire output list into memory. For small or medium-sized lists this is generally fine, but for very large lists it can consume too much memory.

If you want to sum the squares of the first billion integers, a list comprehension would try to create a list with one billion integers:

```
>>> sum([number * number for number in range(1000)])
332833500
```

Instead, use a generator, which doesn’t create a single large data structure in memory but returns an iterable:

```
>>> sum(number * number for number in range(1_000_000_000))
333333332833333333500000000
```

You can tell this is a generator because the expression isn’t inside brackets or curly braces. Generators perform operations lazily—your code only calculates values when they’re explicitly requested. After the generator yields a value, it adds that value to the running sum, then discards that value and generates the next value.

The `map()` function also operates lazily:

```
>>> sum(map(lambda number: number * number, range(1_000_000_000)))
333333332833333333500000000
```

### Profile to Optimize Performance

Which approach is faster? Rather than adhere to a single rule, profile different approaches and listen to the data. The `timeit` library is useful for timing how long it takes chunks of code to run:

```
>>> import random
>>> import timeit
>>> TAX_RATE = .08
>>> PRICES = [random.randrange(100) for _ in range(100_000)]
>>> def get_price(price):
...     return price * (1 + TAX_RATE)
...
>>> def get_prices_with_map():
...     return list(map(get_price, PRICES))
...
>>> def get_prices_with_comprehension():
...     return [get_price(price) for price in PRICES]
...
>>> def get_prices_with_loop():
...     prices = []
...     for price in PRICES:
...         prices.append(get_price(price))
...     return prices
...

>>> timeit.timeit(get_prices_with_map, number=100)
2.0554370979998566

>>> timeit.timeit(get_prices_with_comprehension, number=100)
2.3982384680002724

>>> timeit.timeit(get_prices_with_loop, number=100)
3.0531821520007725
```

The biggest difference is between the loop-based approach and `map()`, with the loop taking 50 percent longer to execute.

## Conclusion

Whenever you have to choose a list creation method, try multiple implementations and consider what’s most convenient to read and understand in your specific scenario. If performance is important, use profiling tools to give you actionable data instead of relying on hunches.

**Now you can:**

- Simplify loops and `map()` calls with declarative list comprehensions
- Supercharge your comprehensions with conditional logic
- Create set and dictionary comprehensions
- Determine when code clarity or performance dictates an alternative approach

## Frequently Asked Questions

**What is a list comprehension in Python?**

A list comprehension is a Python construct that lets you create a new list by applying an expression to each item in an existing iterable, all in a single line of code.

**When should you use a list comprehension instead of a loop?**

You should use a list comprehension when you want to create a list in a concise, readable manner, especially when transforming or filtering elements from an existing iterable.

**How can you add conditional logic to a list comprehension?**

You can add conditional logic by including an `if` statement at the end of the comprehension to filter elements, or you can use a conditional expression within the comprehension to modify elements.

**Is a list comprehension faster than a `for` loop?**

In general, list comprehensions are faster than `for` loops because they’re optimized for performance, but you should profile your specific use case to confirm this.