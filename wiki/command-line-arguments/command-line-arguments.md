# Command-Line Arguments

> Sources: Andre Burgaud (Real Python), 2020-02-05
> Raw: [python-command-line-arguments](../../raw/command-line-arguments/python-command-line-arguments.md)
> Updated: 2026-10-29

## Overview

Python exposes `sys.argv`, a mechanism to capture and extract command-line arguments passed to a program. These values can modify a program’s behavior — for example, passing a filename instead of hard-coding it. Adding command-line argument support gives a text-based program a user-friendly command-line interface (CLI), comparable to what a GUI provides for a visual application.

A CLI is characterized by a command or program, zero or more command-line arguments, an output representing the result, and textual documentation referred to as usage or help.

## Origins and Core Mechanism

Python command-line arguments directly inherit from the C language, where `main(int argc, char *argv[])` receives `argc` (argument count) and `argv` (argument vector, an array with the program name in element 0 followed by the arguments). Python’s equivalent is `sys.argv`:

- `sys.argv[0]` contains the name of the current Python program.
- `sys.argv[1:]` contains all remaining command-line arguments.

Python has no separate `argc` variable; `len(sys.argv)` gives the argument count.

Example:

```
$ python main.py Python Command Line Arguments
Arguments count: 5
Argument      0: main.py
Argument      1: Python
Argument      2: Command
Argument      3: Line
Argument      4: Arguments
```

`sys.argv` is globally available to all modules imported during execution, but it is **not immutable**. In larger programs, store arguments in a separate variable (e.g. `args = sys.argv[1:]`) to protect them from inadvertent mutation — `pip` does exactly this in its `main()` function.

## CLI Anatomy and Conventions

Command-line arguments compose a CLI and can be categorized as:

1. **Options** (flags/switches) — modify program behavior, e.g. `ls -ls`.
2. **Arguments** (operands) — represent the source or destination of data, e.g. `cp main main2`.
3. **Subcommands** — let a program define multiple commands, e.g. `git branch`, `pip install`.

Relevant standards include POSIX Utility Conventions, GNU Standards for Command Line Interfaces, and docopt. Key conventions:

- All options preceded with a hyphen (`-`); GNU adds long options (`--help`, `--version`).
- Option-arguments should not be optional (POSIX).
- Short options can be stacked (`-abc` = `-a -b -c`); long options take arguments after a space or `=`.
- On Windows, the option separator is a forward slash (`/`) instead of a hyphen.

At process start, Python command-line arguments split into Python options (e.g. `-B`, `-v`, `-O`) that influence the interpreter, and the Python program with its own arguments. Within the program, only `sys.argv` is accessible — Python options are not.

## Whitespace Handling

Arguments containing whitespace must be escaped so the shell treats them as one argument:

- Surround with single quotes (`'Real Python'`)
- Surround with double quotes (`"Real Python"`)
- Prefix each space with a backslash (`Real\ Python`)

On Windows, double quotes toggle special-character handling on and off, which can be counterintuitive.

## Error Handling

Command-line arguments are loose strings; missing or invalid arguments cause errors such as `IndexError: list index out of range` when accessing `sys.argv[1]` without an argument. Guard access with `try/except` and `raise SystemExit(f"Usage: {sys.argv[0]} ...")`, exiting with status code 1.

## Parsing Approaches

Several approaches exist, from manual to library-based:

### List comprehensions

For simple cases, separate options from arguments with list comprehensions:

```
opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]
```

This fails when order matters, option-arguments are needed, or arguments are prefixed with a hyphen.

### Regular expressions

A regex can enforce order, specific options/option-arguments, and argument types. Example: a `seq`-like program capturing `--help`, `-s`/`--separator`, and up to three integer operands via named groups (`HELP`, `SEP`, `OP1`–`OP3`). Arguments are joined into one string (`" ".join(sys.argv[1:])`) before matching.

### Custom parsers

A loop using `collections.deque` and `popleft()` fetches each argument and applies custom semantics. This works for simple cases but becomes error-prone with many arguments, complex interdependencies, or validation requirements — it isn’t reusable.

## File Handling and Standard Streams

### Files

Scripts can process one or more files passed as arguments (e.g. a `sha1sum` clone computing SHA-1 hashes per file). Shells perform wildcard expansion on Unix-like systems; on Windows, use `glob.glob()` to expand wildcards internally.

### Standard input

With no arguments, a program can read from `sys.stdin`. A hyphen (`-`) as a file argument conventionally means the program reads from the standard input.

### Standard output and standard error

Following the Unix Philosophy, send debug/trace output to `sys.stderr` so it doesn’t contaminate `stdout` when programs are chained with pipes:

```
print("DEBUG ...", file=sys.stderr)
```

## Validation

Validate argument count and type. All `sys.argv` items are strings, so convert as needed (e.g. `str.isdigit()` then `int()`). Python data classes or `NamedTuple` can enforce field count and types. Custom validation can catch `FileNotFoundError`/`IsADirectoryError` for bad filenames and report to `stderr`.

## Standard Library

### argparse

The recommended standard-library module (Python 3.2+ supersedes the deprecated `optparse`; `getopt` also exists). Example:

```
parser = argparse.ArgumentParser(
    usage="%(prog)s [OPTION] [FILE]...",
    description="Print or check SHA1 (160-bit) checksums."
)
parser.add_argument("-v", "--version", action="version", version="1.0.0")
parser.add_argument("files", nargs="*")
args = parser.parse_args()
```

`argparse` provides `--help` and `--version` for free and populates an `argparse.Namespace` with parsed fields.

### getopt

Originates from the C `getopt` function. `getopt.getopt(sys.argv[1:], short_opts, long_opts)` where a short option followed by `:` expects an argument, and a long option trailed with `=` expects an argument.

## External Packages

- **Click** — decorators (`@click.command`, `@click.option`, `@click.argument`) build sophisticated CLIs with minimal boilerplate; used by Flask and Black. Supports output coloring, prompts, subcommands, type validation, callbacks, file path validation, progress bars. Set `ignore_unknown_options=True` so negative integers aren’t parsed as options.
- **Python Prompt Toolkit** — dialog-based (`button_dialog`, `input_dialog`, `message_dialog`) text user interfaces as an alternative to strict CLI conventions.
- Others: Typer, Plac, Cliff, Cement, Python Fire.

## See Also

- [Mastering Python Collections](../python-collections/mastering-python-collections.md) — Exercise 0 (Command Quest) introduces `sys.argv`; list comprehensions used for parsing options.
- [Walrus Operator](../assignment-expressions/walrus-operator.md) — assignment expressions usable inside list comprehensions for parsing.
