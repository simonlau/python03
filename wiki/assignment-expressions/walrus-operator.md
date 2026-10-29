# Walrus Operator

> Sources: Geir Arne Hjelle (Real Python), 2024-12-14
> Raw: [the-walrus-operator-pythons-assignment-expressions](../../raw/assignment-expressions/the-walrus-operator-pythons-assignment-expressions.md)
> Updated: 2026-10-29

## Overview

The walrus operator (`:=`), formally known as the assignment expression operator, lets you assign values to variables as part of an expression in Python. Introduced in Python 3.8 via PEP 572, it combines assignment and evaluation in a single statement so you can avoid repetitive function calls or calculations. Assignment expressions return the value being assigned, unlike regular assignment statements, which return nothing. The operator is nicknamed the walrus operator because `:=` resembles the eyes and tusks of a walrus lying on its side; it is also called the colon equals operator or named expressions.

## Core Behavior

An assignment expression assigns a value to a variable and returns that value. Because it is an expression (not a statement), it can appear inside other expressions such as conditions, comprehensions, and function arguments. A bare `walrus := True` is a `SyntaxError`; you must wrap it in parentheses, e.g. `(walrus := True)`. The walrus operator is never a direct replacement for the `=` assignment statement, and vice versa.

PEP 572 was written by Chris Angelico in February 2018, accepted by Guido van Rossum in July 2018, and implemented by Emily Morehouse for the first alpha of Python 3.8. Since early 2019, Python has been governed by an elected steering council rather than a BDFL.

## Use Cases

### Debugging complex expressions

The walrus operator shines when debugging: you can name a subexpression inside a larger expression and inspect it afterward without duplicating the calculation. For example, when computing the haversine distance between Oslo and Vancouver (just under 7,200 km), you can capture the intermediate `ϕ_hav` term inside the `sqrt()` call and print it afterward to confirm the implementation.

### Avoiding repeated calls

A common pattern is computing a value once and reusing it. With a dictionary of descriptive statistics, instead of calling `len(numbers)` and `sum(numbers)` twice, you can bind them inline:

```
description = {
    "length": (num_length := len(numbers)),
    "sum": (num_sum := sum(numbers)),
    "mean": num_sum / num_length,
}
```

The same idea applies to reading a file once in a `wc`-style line/word/character counter rather than calling `path.read_text()` three times. The source notes that a plain separate assignment may strike a better balance between readability and conciseness.

### List comprehensions

When filtering on the result of an expensive function, the walrus operator avoids calling the function twice:

```
results = [value for num in numbers if (value := slow(num)) > 0]
```

The parentheses are required. Placing the assignment in the expression position (`[(value := slow(num)) for ...]`) raises a `NameError` because the `if` clause is evaluated first. The same principle applies to dictionary comprehensions, set comprehensions, and generator expressions — for example, computing the average length of podcast titles over 50 characters without calling `len()` twice yields `61.525`.

### While loops

A `while` loop that reads input and validates it normally repeats the `input()` call. The walrus operator folds the read and check into the condition:

```
while (user_answer := input(f"\n{question} ")) not in valid_answers:
    print(f"Please answer one of {', '.join(valid_answers)}")
```

### Witnesses and counterexamples with any()/all()

Because `any()` and `all()` short-circuit, you can capture the last item checked — a witness (for `any()`) or counterexample (for `all()`) — directly inside the expression:

```
if any((witness := city).startswith("B") for city in cities):
    print(f"{witness} starts with B")
```

Only the last item evaluated survives in `witness`, so when `any()` returns `False` the captured value may not satisfy the condition.

## Syntax Restrictions

Assignment expressions are illegal or discouraged in several contexts:

- As a standalone statement without parentheses: `walrus := True` → `SyntaxError`.
- Chained assignment: `lat = lon := 0` → `SyntaxError`.
- As keyword arguments or default parameter values: `angle(phi = lat := 59.9)` → `SyntaxError`.
- Attribute or item assignment: `(mapping["hearts"] := "♥")` → `SyntaxError`.
- Iterable unpacking: `lat, lon := 59.9, 10.8` → `SyntaxError`.
- Augmented assignment: `count +:= 1` → `SyntaxError` (PEP 577 for augmented assignment expressions was withdrawn).

Within f-strings, `:=` already has a meaning (format specification alignment), so assignment expressions need parentheses: `f"{(x := 8)}"`.

The walrus operator binds less tightly than all other operators except the comma, so `if square := number ** 2 > 5:` binds `square` to the boolean result, not to `number ** 2`. Use parentheses: `if (square := number ** 2) > 5:`. When assigning a tuple, always parenthesize the tuple: `(walrus := (3.8, True))`.

## Scope and Precedence

The scope of an assignment target follows the LEGB rule, honoring `global` and `nonlocal` declarations just like a regular assignment. Style guidance: always add spaces around `:=`, and use parentheses only as needed.

## Pitfalls

The walrus operator is available only in Python 3.8 and later, so code using `:=` is incompatible with older versions. The operator will not revolutionize Python; it enables small improvements where useful, and you should avoid overusing it when a traditional assignment is clearer.

## See Also
