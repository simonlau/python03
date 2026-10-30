# Generating Random Data in Python

> Sources: Brad Solomon (Real Python), 2018-07-11
> Raw: [generating-random-data-python](../../raw/random-data/generating-random-data-python.md)
> Updated: 2026-10-30

## Overview

Python offers several options for generating random data, each with different levels of security, versatility, purpose, and speed. Most random data generated with Python is **pseudorandom** — generated with a pseudorandom number generator (PRNG), an algorithm for generating seemingly random but still reproducible data. “True” random numbers require a true random number generator (TRNG), such as hardware-based sources, which are out of scope here.

Use plain PRNGs for statistical modeling, simulation, and making random data reproducible; they’re significantly faster than CSPRNGs. Use cryptographically secure PRNGs (CSPRNGs) for security and cryptographic applications where data sensitivity is imperative.

## PRNGs in Python

### The `random` Module

Python’s `random` module uses the Mersenne Twister PRNG algorithm as its core generator. Its documentation warns: “The pseudo-random generators of this module should not be used for security purposes.”

**Seeding.** `random.seed()` makes results reproducible — the same seed always produces the same sequence:

```python
>>> random.seed(444)
>>> random.random()
0.3088946587429545
>>> random.random()
0.01323751590501987

>>> random.seed(444)  # Re-seed
>>> random.random()
0.3088946587429545
>>> random.random()
0.01323751590501987
```

Without seeding, the generator uses the current system time or an OS randomness source.

**Core functions:**

| Function | Description |
| --- | --- |
| `random.random()` | Random float in [0.0, 1.0) |
| `random.randint(a, b)` | Random integer in [a, b], inclusive |
| `random.randrange(a, b)` | Random integer in [a, b), right-exclusive |
| `random.uniform(a, b)` | Random float in [a, b] |
| `random.choice(seq)` | Random element from a non-empty sequence |
| `random.choices(seq, k)` | Random k elements with replacement |
| `random.sample(pop, k)` | Random k elements without replacement |
| `random.shuffle(x)` | Shuffle a sequence in place |

To avoid mutating the original list with `shuffle()`, make a copy first (e.g., `x[:]` or `x.copy()`).

### Generating Unique Random Strings

A Python `set` works well for membership testing when generating unique random strings:

```python
import string

def unique_strings(k: int, ntokens: int,
               pool: str=string.ascii_letters) -> set:
    seen = set()
    join = ''.join
    add = seen.add
    while len(seen) < ntokens:
        token = join(random.choices(pool, k=k))
        add(token)
    return seen
```

Python’s `string` module provides constants such as `ascii_lowercase`, `ascii_uppercase`, `punctuation`, and `ascii_whitespace`.

### `numpy.random`

`numpy.random` is like `random` but for NumPy arrays, with its own separate PRNG — `random.seed()` does not affect it. It supports many more statistical distributions and is specialized for large, multidimensional arrays. For a single value or small sequence, the standard-library `random` is typically faster (NumPy has overhead).

```python
>>> np.random.seed(444)
>>> np.random.randn(5)
array([ 0.36,  0.38,  1.38,  1.18, -0.94])
```

NumPy’s `randint` is [inclusive, exclusive), unlike `random.randint()`.

## CSPRNGs in Python

### `os.urandom()`

Generates operating-system-dependent random bytes that are safely cryptographically secure:

- Unix: reads from `/dev/urandom`
- Windows: uses `CryptGenRandom()`

No manual seeding; the only argument is the number of bytes to return:

```python
>>> os.urandom(3)
b'\xa2\xe8\x02'
>>> x = os.urandom(6)
>>> x.hex()
'ce11e7222184'
```

Each byte maps to an integer between 0 and 255; two hex digits correspond to one byte.

### `secrets`

Introduced in Python 3.6 (PEP 506), `secrets` is the de facto module for generating cryptographically secure random bytes and strings. It’s a wrapper around `os.urandom()`:

```python
>>> n = 16
>>> secrets.token_bytes(n)
b'A\x8cz\xe1o\xf9!;\x8b\xf2\x80pJ\x8b\xd4\xd3'
>>> secrets.token_hex(n)
'9cb190491e01230ec4239cae643f286f'
>>> secrets.token_urlsafe(n)
'MJoi7CknFu3YN41m88SEgQ'
>>> secrets.choice('rain')
'a'
```

`token_urlsafe()` uses base64 encoding; for `nbytes` bytes the length is `math.ceil(nbytes * 8 / 6)`.

Example — a URL shortener:

```python
from secrets import token_urlsafe

DATABASE = {}

def shorten(url: str, nbytes: int = 5) -> str:
    ext = token_urlsafe(nbytes=nbytes)
    if ext in DATABASE:
        return shorten(url, nbytes=nbytes)
    DATABASE.update({ext: url})
    return f'short.ly/{ext}'
```

### `uuid`

The `uuid4()` function generates a 128-bit Universally Unique IDentifier using `os.urandom()`:

```python
>>> import uuid
>>> uuid.uuid4()
UUID('3e3ef28d-3ff0-4933-9bba-e5ee91ce0e7b')
```

There are `2 ** 128` possible `uuid4` values. Other variations: `uuid1()` (host ID + current time), `uuid3()` (MD5), `uuid5()` (SHA-1).

### Why Not Just “Default to” `SystemRandom`?

`random.SystemRandom()` uses `os.urandom()`. Reasons not to default to it:

1. Sometimes you want deterministic, reproducible data.
2. CSPRNGs are meaningfully slower: roughly 5x slower than PRNGs in a timing comparison with 1,000,000 loops.

## Odds and Ends: Hashing

Hashing via Python’s `hashlib` module is a one-way mapping from input to a fixed-size string. A hash may “look like” random data but doesn’t qualify as random under the definition here.

## Recap

| Package/Module | Description | Cryptographically Secure |
| --- | --- | --- |
| `random` | Fast & easy random data using Mersenne Twister | No |
| `numpy.random` | Like `random` but for arrays | No |
| `os` | Contains `urandom()` | Yes |
| `secrets` | De facto module for secure random numbers, bytes, strings | Yes |
| `uuid` | Functions for building 128-bit identifiers | Yes, `uuid4()` |

## See Also

- [Mastering Python Collections](../python-collections/mastering-python-collections.md) — collections (lists, tuples, sets, dicts) used with `random.choice()`, `random.sample()`, and `random.shuffle()`.
- [Python Set](../python-collections/python-set.md) — sets used for membership testing when generating unique random strings.
- [Python Generators](../python-collections/python-generators.md) — generator expressions can feed data into `random`-based pipelines.
