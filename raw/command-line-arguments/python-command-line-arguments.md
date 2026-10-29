# Python Command-Line Arguments

> Source: https://realpython.com/python-command-line-arguments/
> Collected: 2026-10-29
> Published: Unknown

Adding the capability of processing Python command-line arguments provides a user-friendly interface to your text-based command line program. It’s similar to what a graphical user interface is for a visual application that’s manipulated by graphical elements or widgets.

Python exposes a mechanism to capture and extract your Python command-line arguments. These values can be used to modify the behavior of a program. For example, if your program processes data read from a file, then you can pass the name of the file to your program, rather than hard-coding the value in your source code.

**By the end of this tutorial, you’ll know:**

- **The origins** of Python command-line arguments

- **The underlying support** for Python command-line arguments

- **The standards** guiding the design of a command-line interface

- **The basics** to manually customize and handle Python command-line arguments

- **The libraries** available in Python to ease the development of a complex command-line interface

## The Command-Line Interface

A command-line interface (CLI) provides a way for a user to interact with a program running in a text-based shell interpreter. Some examples of shell interpreters are Bash on Linux or Command Prompt on Windows. A command-line interface is enabled by the shell interpreter that exposes a command prompt. It can be characterized by the following elements:

- A command or program
- Zero or more command line arguments
- An output representing the result of the command
- Textual documentation referred to as usage or help

Not every command-line interface may provide all these elements, but this list isn’t exhaustive, either. The complexity of the command line ranges from the ability to pass a single argument, to numerous arguments and options, much like a Domain Specific Language.

The two following examples with the Python command illustrates the description of a command-line interface:

```
$ python -c "print('Real Python')"
Real Python
```

In this first example, the Python interpreter takes option `-c` for command, which says to execute the Python command-line arguments following the option `-c` as a Python program.

Another example shows how to invoke Python with `-h` to display the help:

```
$ python -h
usage: python3 [option] ... [-c cmd | -m mod | file | -] [arg] ...
```

## The C Legacy

Python command-line arguments directly inherit from the C programming language. As Guido Van Rossum wrote in An Introduction to Python for Unix/C Programmers in 1993, C had a strong influence on Python. Guido mentions the definitions of literals, identifiers, operators, and statements like break, continue, or return. The use of Python command-line arguments is also strongly influenced by the C language.

To illustrate the similarities, consider the following C program:

```
// main.c
#include <stdio.h>

int main(int argc, char *argv[]) {
   printf("Arguments count: %d\n", argc);
   for (int i = 0; i < argc; i++) {
       printf("Argument %6d: %s\n", i, argv[i]);
   }
   return 0;
}
```

Line 4 defines main(), which is the entry point of a C program. Take good note of the parameters:

1. argc is an integer representing the number of arguments of the program.
2. argv is an array of pointers to characters containing the name of the program in the first element of the array, followed by the arguments of the program, if any, in the remaining elements of the array.

Note: argc stands for argument count, while argv stands for argument vector.

You could implement a Python program, main.py, that’s equivalent to the C program:

```
# main.py
import sys

if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")
```

You don’t see an argc variable like in the C code example. It doesn’t exist in Python because sys.argv is sufficient. You can parse the Python command-line arguments in sys.argv without having to know the length of the list, and you can call the built-in len() if the number of arguments is needed by your program.

Execute main.py as follows:

```
$ python main.py Python Command Line Arguments
Arguments count: 5
Argument      0: main.py
Argument      1: Python
Argument      2: Command
Argument      3: Line
Argument      4: Arguments
```

sys.argv contains the same information as in the C program:

- The name of the program main.py is the first item of the list.
- The arguments Python, Command, Line, and Arguments are the remaining elements in the list.

## Two Utilities From the Unix World

To use Python command-line arguments in this tutorial, you’ll implement some partial features of two utilities from the Unix ecosystem:

1. sha1sum
2. seq

You’ll gain some familiarity with these Unix tools in the following sections.

### sha1sum

sha1sum calculates SHA-1 hashes, and it’s often used to verify the integrity of files. For a given input, a hash function always returns the same value. Any minor changes in the input will result in a different hash value.

To calculate the SHA-1 hash value of the content of a file, you proceed as follows:

```
$ sha1sum main.c
125a0f900ff6f164752600550879cbfabb098bc3  main.c
```

The result shows the SHA-1 hash value as the first field and the name of the file as the second field. The command can take more than one file as arguments:

```
$ sha1sum main.c main.py
125a0f900ff6f164752600550879cbfabb098bc3  main.c
d84372fc77a90336b6bb7c5e959bcb1b24c608b4  main.py
```

Thanks to the wildcards expansion feature of the Unix terminal, it’s also possible to provide Python command-line arguments with wildcard characters. One such a character is the asterisk or star (*):

```
$ sha1sum main.*
3f6d5274d6317d580e2ffc1bf52beee0d94bf078  main.c
f41259ea5835446536d2e71e566075c1c1bfc111  main.py
```

Without any argument, sha1sum reads from the standard input.

### seq

seq generates a sequence of numbers. In its most basic form, like generating the sequence from 1 to 5, you can execute the following:

```
$ seq 5
1
2
3
4
5
```

## The sys.argv Array

Before exploring some accepted conventions and discovering how to handle Python command-line arguments, you need to know that the underlying support for all Python command-line arguments is provided by sys.argv. The examples in the following sections show you how to handle the Python command-line arguments stored in sys.argv and to overcome typical issues that occur when you try to access them.

### Displaying Arguments

The sys module exposes an array named argv that includes the following:

1. argv[0] contains the name of the current Python program.
2. argv[1:], the rest of the list, contains any and all Python command-line arguments passed to the program.

The following example demonstrates the content of sys.argv:

```
# argv.py
import sys

print(f"Name of the script      : {sys.argv[0]=}")
print(f"Arguments of the script : {sys.argv[1:]=}")
```

Line 2 imports the internal Python module sys.
Line 4 extracts the name of the program by accessing the first element of the list sys.argv.
Line 5 displays the Python command-line arguments by fetching all the remaining elements of the list sys.argv.

Note: The f-string syntax used in argv.py leverages the new debugging specifier in Python 3.8. If your Python version is less than 3.8, then simply remove the equals sign (=) in both f-strings to allow the program to execute successfully.

Execute the script argv.py above with a list of arbitrary arguments as follows:

```
$ python argv.py un deux trois quatre
Name of the script      : sys.argv[0]='argv.py'
Arguments of the script : sys.argv[1:]=['un', 'deux', 'trois', 'quatre']
```

### Reversing the First Argument

The example reverse.py reverses the first argument passed at the command line:

```
# reverse.py

import sys

arg = sys.argv[1]
print(arg[::-1])
```

In reverse.py the process to reverse the first argument is performed with the following steps:

- Line 5 fetches the first argument of the program stored at index 1 of sys.argv. Remember that the program name is stored at index 0 of sys.argv.
- Line 6 prints the reversed string.

You execute the script as follows:

```
$ python reverse.py "Real Python"
nohtyP laeR
```

Note that surrounding the multi-word string "Real Python" with quotes ensures that the interpreter handles it as a unique argument, instead of two arguments.

### Mutating sys.argv

sys.argv is globally available to your running Python program. All modules imported during the execution of the process have direct access to sys.argv. This global access might be convenient, but sys.argv isn’t immutable.

Observe what happens if you tamper with sys.argv:

```
# argv_pop.py

import sys

print(sys.argv)
sys.argv.pop()
print(sys.argv)
```

Execute the script above:

```
$ python argv_pop.py un deux trois quatre
['argv_pop.py', 'un', 'deux', 'trois', 'quatre']
['argv_pop.py', 'un', 'deux', 'trois']
```

Notice that the fourth argument is no longer included in sys.argv.

In a short script, you can safely rely on the global access to sys.argv, but in a larger program, you may want to store arguments in a separate variable:

```
# argv_var_pop.py

import sys

print(sys.argv)
args = sys.argv[1:]
print(args)
sys.argv.pop()
print(sys.argv)
print(args)
```

This time, although sys.argv lost its last element, args has been safely preserved. args isn’t global, and you can pass it around to parse the arguments per the logic of your program. The Python package manager, pip, uses this approach. Here’s a short excerpt of the pip source code:

```
def main(args=None):
    if args is None:
        args = sys.argv[1:]
```

main() saves into args the slice of sys.argv that contains only the arguments and not the file name. sys.argv remains untouched, and args isn’t impacted by any inadvertent changes to sys.argv.

### Escaping Whitespace Characters

In the reverse.py example, the first and only argument is "Real Python", and the result is "nohtyP laeR". The argument includes a whitespace separator between "Real" and "Python", and it needs to be escaped.

On Linux, whitespaces can be escaped by doing one of the following:

1. Surrounding the arguments with single quotes (')
2. Surrounding the arguments with double quotes (")
3. Prefixing each space with a backslash (\)

Without one of the escape solutions, reverse.py stores two arguments, "Real" in sys.argv[1] and "Python" in sys.argv[2]:

```
$ python reverse.py Real Python
laeR
```

The output above shows that the script only reverses "Real" and that "Python" is ignored. To ensure both arguments are stored, you’d need to surround the overall string with double quotes (").

You can also use a backslash (\) to escape the whitespace:

```
$ python reverse.py Real\ Python
nohtyP laeR
```

In Unix shells, the internal field separator (IFS) defines characters used as delimiters. From the result of `printf "%q\n" "$IFS"`, which is $' \t\n', you identify three delimiters:

1. Space (' ')
2. Tab (\t)
3. Newline (\n)

Prefixing a space with a backslash (\) bypasses the default behavior of the space as a delimiter in the string "Real Python". This results in one block of text as intended, instead of two.

Note that, on Windows, the whitespace interpretation can be managed by using a combination of double quotes.

### Handling Errors

Python command-line arguments are loose strings. Many things can go wrong, so it’s a good idea to provide the users of your program with some guidance in the event they pass incorrect arguments at the command line. For example, reverse.py expects one argument, and if you omit it, then you get an error:

```
 1$ python reverse.py
 2Traceback (most recent call last):
 3  File "reverse.py", line 5, in <module>
 4    arg = sys.argv[1]
 5IndexError: list index out of range
```

The Python exception IndexError is raised, and the corresponding traceback shows that the error is caused by the expression arg = sys.argv[1]. The message of the exception is list index out of range. You didn’t pass an argument at the command line, so there’s nothing in the list sys.argv at index 1.

This is a common pattern that can be addressed in a few different ways. For this initial example, you’ll keep it brief by including the expression arg = sys.argv[1] in a try block:

```
# reverse_exc.py

import sys

try:
    arg = sys.argv[1]
except IndexError:
    raise SystemExit(f"Usage: {sys.argv[0]} <string_to_reverse>")
print(arg[::-1])
```

The expression on line 4 is included in a try block. Line 8 raises the built-in exception SystemExit. If no argument is passed to reverse_exc.py, then the process exits with a status code of 1 after printing the usage. Note the integration of sys.argv[0] in the error message. It exposes the name of the program in the usage message.

Now, when you execute the same program without any Python command-line arguments, you can see the following output:

```
$ python reverse.py
Usage: reverse.py <string_to_reverse>

$ echo $?
1
```

### Calculating the sha1sum

You’ll write another script to demonstrate that, on Unix-like systems, Python command-line arguments are passed by bytes from the OS. This script takes a string as an argument and outputs the hexadecimal SHA-1 hash of the argument:

```
# sha1sum.py

import sys
import hashlib

data = sys.argv[1]
m = hashlib.sha1()
m.update(bytes(data, 'utf-8'))
print(m.hexdigest())
```

When you run the script with an argument, you get this:

```
$ python sha1sum.py "Real Python"
0554943d034f044c5998f55dac8ee2c03e387565
```

Note: Checkout hashlib for more details about the hash functions available in the Python standard library.

From the sys.argv documentation, you learn that in order to get the original bytes of the Python command-line arguments, you can use os.fsencode(). By directly obtaining the bytes from sys.argv[1], you don’t need to perform the string-to-bytes conversion of data:

```
# sha1sum_bytes.py

import os
import sys
import hashlib

data = os.fsencode(sys.argv[1])
m = hashlib.sha1()
m.update(data)
print(m.hexdigest())
```

Execute sha1sum_bytes.py to compare the output:

```
$ python sha1sum_bytes.py "Real Python"
0554943d034f044c5998f55dac8ee2c03e387565
```

The hexadecimal value of the SHA1 hash is the same as in the previous sha1sum.py example.

## The Anatomy of Python Command-Line Arguments

Now that you’ve explored a few aspects of Python command-line arguments, most notably sys.argv, you’re going to apply some of the standards that are regularly used by developers while implementing a command-line interface.

Python command-line arguments are a subset of the command-line interface. They can be composed of different types of arguments:

1. Options modify the behavior of a particular command or program.
2. Arguments represent the source or destination to be processed.
3. Subcommands allow a program to define more than one command with the respective set of options and arguments.

Before you go deeper into the different types of arguments, you’ll get an overview of the accepted standards that have been guiding the design of the command-line interface and arguments. These have been refined since the advent of the computer terminal in the mid-1960s.

### Standards

A few available standards provide some definitions and guidelines to promote consistency for implementing commands and their arguments. These are the main UNIX standards and references:

- POSIX Utility Conventions
- GNU Standards for Command Line Interfaces
- docopt

The following points are examples taken from those references:

- POSIX:
  - A program or utility is followed by options, option-arguments, and operands.
  - All options should be preceded with a hyphen or minus (-) delimiter character.
  - Option-arguments should not be optional.

- GNU:
  - All programs should support two standard options, which are --version and --help.
  - Long-named options are equivalent to the single-letter Unix-style options. An example is --debug and -d.

- docopt:
  - Short options can be stacked, meaning that -abc is equivalent to -a -b -c.
  - Long options can have arguments specified after a space or the equals sign (=). The long option --input=ARG is equivalent to --input ARG.

**Note:** You don’t need to follow those standards rigorously. Instead, follow the conventions that have been used successfully for years since the advent of UNIX. If you write a set of utilities for you or your team, then ensure that you stay consistent across the different utilities.

### Options

An option, sometimes called a flag or a switch, is intended to modify the behavior of the program. For example, the command ls on Linux lists the content of a given directory.

An option can take an argument, which is called an option-argument. See an example in action with od below:

```
$ od -t x1z -N 16 main
0000000 7f 45 4c 46 02 01 01 00 00 00 00 00 00 00 00 00  >.ELF............<
```

od stands for octal dump. This utility displays data in different printable representations, like octal (which is the default), hexadecimal, decimal, and ASCII. In the example above, it takes the binary file main and displays the first 16 bytes of the file in hexadecimal format. The option -t expects a type as an option-argument, and -N expects the number of input bytes.

In the example above, -t is given type x1, which stands for hexadecimal and one byte per integer. This is followed by z to display the printable characters at the end of the input line. -N takes 16 as an option-argument for limiting the number of input bytes to 16.

### Arguments

The arguments are also called operands or parameters in the POSIX standards. The arguments represent the source or the destination of the data that the command acts on. For example, the command cp, which is used to copy one or more files to a file or a directory, takes at least one source and one target:

```
$ ls main
main

$ cp main main2

$ ls -lt
main
main2
...
```

In line 4, cp takes two arguments:

1. main: the source file
2. main2: the target file

It then copies the content of main to a new file named main2. Both main and main2 are arguments, or operands, of the program cp.

### Subcommands

The concept of subcommands isn’t documented in the POSIX or GNU standards, but it does appear in docopt. The standard Unix utilities are small tools adhering to the Unix philosophy. Unix programs are intended to be programs that do one thing and do it well. This means no subcommands are necessary.

By contrast, a new generation of programs, including git, go, docker, and gcloud, come with a slightly different paradigm that embraces subcommands. Take git as an example. It handles several commands, each possibly with their own set of options, option-arguments, and arguments. The following examples apply to the git subcommand branch:

- git branch displays the branches of the local git repository.
- git branch custom_python creates a local branch custom_python in a local repository.
- git branch -d custom_python deletes the local branch custom_python in a local repository.
- git branch --help displays the help for the git branch subcommand.

In the Python ecosystem, pip has the concept of subcommands, too. Some pip subcommands include list, install, freeze, or uninstall.

### Windows

On Windows, the conventions regarding Python command-line arguments are slightly different, in particular, those regarding command line options. Note that the separator for an option is a forward slash (/) instead of a hyphen (-) like the conventions for Unix systems.

### Visuals

At the start of a Python process, Python command-line arguments are split into two categories:

1. Python options: These influence the execution of the Python interpreter. For example, adding option -O is a means to optimize the execution of a Python program by removing assert and __debug__ statements.
2. Python program and its arguments: Following the Python options (if there are any), you’ll find the Python program, which is a file name that usually has the extension .py, and its arguments. By convention, those can also be composed of options and arguments.

Take the following command that’s intended to execute the program main.py, which takes options and arguments:

```
$ python -B -v main.py --verbose --debug un deux
```

In the command line above, the options are Python command-line arguments and are organized as follows:

- The option -B tells Python not to write .pyc files on the import of source modules.
- The option -v stands for verbose and tells Python to trace all import statements.
- The arguments passed to main.py are fictitious and represent two long options (--verbose and --debug) and two arguments (un and deux).

Within the Python program main.py, you only have access to the Python command-line arguments inserted by Python in sys.argv. The Python options may influence the behavior of the program but are not accessible in main.py.

## A Few Methods for Parsing Python Command-Line Arguments

Now you’re going to explore a few approaches to apprehend options, option-arguments, and operands. This is done by parsing Python command-line arguments.

For something uncomplicated, the following pattern, which doesn’t enforce ordering and doesn’t handle option-arguments, may be enough:

```
# cul.py

import sys

opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

if "-c" in opts:
    print(" ".join(arg.capitalize() for arg in args))
elif "-u" in opts:
    print(" ".join(arg.upper() for arg in args))
elif "-l" in opts:
    print(" ".join(arg.lower() for arg in args))
else:
    raise SystemExit(f"Usage: {sys.argv[0]} (-c | -u | -l) <arguments>...")
```

The intent of the program above is to modify the case of the Python command-line arguments. Three options are available:

- -c to capitalize the arguments
- -u to convert the arguments to uppercase
- -l to convert the argument to lowercase

The code collects and separates the different argument types using list comprehensions:

- Line 5 collects all the options by filtering on any Python command-line arguments starting with a hyphen (-).
- Line 6 assembles the program arguments by filtering out the options.

When you execute the Python program above with a set of options and arguments, you get the following output:

```
$ python cul.py -c un deux trois
Un Deux Trois
```

This approach might suffice in many situations, but it would fail in the following cases:

- If the order is important, and in particular, if options should appear before the arguments
- If support for option-arguments is needed
- If some arguments are prefixed with a hyphen (-)

### Regular Expressions

You can use a regular expression to enforce a certain order, specific options and option-arguments, or even the type of arguments. To illustrate the usage of a regular expression to parse Python command-line arguments, you’ll implement a Python version of seq, which is a program that prints a sequence of numbers.

First, look at a regular expression that’s intended to capture the requirements above:

```
args_pattern = re.compile(
    r"""
    ^
    (
        (--(?P<HELP>help).*)|
        ((?:-s|--separator)\s(?P<SEP>.*?)\s)?
        ((?P<OP1>-?\d+))(\s(?P<OP2>-?\d+))?(\s(?P<OP3>-?\d+))?
    )
    $
""",
    re.VERBOSE,
)
```

The regular expression captures and enforces a few aspects of the requirements given for seq. In particular, the command may take:

1. A help option, in short (-h) or long format (--help), captured as a named group called HELP
2. A separator option, -s or --separator, taking an optional argument, and captured as named group called SEP
3. Up to three integer operands, respectively captured as OP1, OP2, and OP3

For clarity, the pattern args_pattern above uses the flag re.VERBOSE on line 11. This allows you to spread the regular expression over a few lines to enhance readability.

For the regular expression to be able to handle these things, it needs to see all Python command-line arguments in one string. You can collect them using str.join():

```
arg_line = " ".join(sys.argv[1:])
```

This makes arg_line a string that includes all arguments, except the program name, separated by a space.

Given the pattern args_pattern above, you can extract the Python command-line arguments with the following function:

```
def parse(arg_line: str) -> Dict[str, str]:
    args: Dict[str, str] = {}
    if match_object := args_pattern.match(arg_line):
        args = {k: v for k, v in match_object.groupdict().items()
                if v is not None}
    return args
```

The pattern is already handling the order of the arguments, mutual exclusivity between options and arguments, and the type of the arguments. parse() is applying re.match() to the argument line to extract the proper values and store the data in a dictionary.

The dictionary includes the names of each group as keys and their respective values. For example, if the arg_line value is --help, then the dictionary is {'HELP': 'help'}. If arg_line is -s T 10, then the dictionary becomes {'SEP': 'T', 'OP1': '10'}.

You can execute the code above by running this command:

```
$ python seq_regex.py 3
```

This should output the following:

```
1
2
3
```

### File Handling

It’s time now to experiment with Python command-line arguments that are expected to be file names. Modify sha1sum.py to handle one or more files as arguments. You’ll end up with a downgraded version of the original sha1sum utility, which takes one or more files as arguments and displays the hexadecimal SHA1 hash for each file, followed by the name of the file:

```
# sha1sum_file.py

import hashlib
import sys

def sha1sum(filename: str) -> str:
    hash = hashlib.sha1()
    with open(filename, mode="rb") as f:
        hash.update(f.read())
    return hash.hexdigest()

for arg in sys.argv[1:]:
    print(f"{sha1sum(arg)}  {arg}")
```

Because you interact with the shell interpreter or the Windows command prompt, you also get the benefit of the wildcard expansion provided by the shell.

The wildcard expansion isn’t available on Windows. To obtain the same behavior, you need to implement it in your code. To refactor main.py to work with wildcard expansion, you can use glob:

```
# main_win.py

import sys
import glob
import itertools
from typing import List

def expand_args(args: List[str]) -> List[str]:
    arguments = args[:1]
    glob_args = [glob.glob(arg) for arg in args[1:]]
    arguments += itertools.chain.from_iterable(glob_args)
    return arguments
```

If you don’t pass any parameter to the original sha1sum utility, then it expects to read data from the standard input. This is the text you enter at the terminal that ends when you type Ctrl+D on Unix-like systems or Ctrl+Z on Windows.

### Standard Input

When you modify the previous Python implementation of sha1sum to handle the standard input using sys.stdin, you’ll get closer to the original sha1sum:

```
# sha1sum_stdin.py

from typing import List
import hashlib
import pathlib
import sys

def process_file(filename: str) -> bytes:
    return pathlib.Path(filename).read_bytes()

def process_stdin() -> bytes:
    return bytes("".join(sys.stdin), "utf-8")

def sha1sum(data: bytes) -> str:
    sha1_hash = hashlib.sha1()
    sha1_hash.update(data)
    return sha1_hash.hexdigest()

def output_sha1sum(data: bytes, filename: str = "-") -> None:
    print(f"{sha1sum(data)}  {filename}")

def main(args: List[str]) -> None:
    if not args:
        args = ["-"]
    for arg in args:
        if arg == "-":
            output_sha1sum(process_stdin(), "-")
        else:
            output_sha1sum(process_file(arg), arg)

if __name__ == "__main__":
    main(sys.argv[1:])
```

Two conventions are applied to this new sha1sum version:

1. Without any arguments, the program expects the data to be provided in the standard input, sys.stdin, which is a readable file object.
2. When a hyphen (-) is provided as a file argument at the command line, the program interprets it as reading the file from the standard input.

### Standard Output and Standard Error

Command line processing may have a direct relationship with stdin to respect the conventions detailed in the previous section. The standard output, although not immediately relevant, is still a concern if you want to adhere to the Unix Philosophy. To allow small programs to be combined, you may have to take into account the three standard streams:

1. stdin
2. stdout
3. stderr

The output of a program becomes the input of another one, allowing you to chain small utilities. For example, if you wanted to sort the aphorisms of the Zen of Python, then you could execute the following:

```
$ python -c "import this" | sort
```

Now, if you want to sort the list of aphorisms, then execute the command as follows:

```
$ python zen_sort_debug.py | sort
```

You may realize that you didn’t intend to have the debug output as the input of the sort command. To address this issue, you want to send traces to the standard errors stream, stderr, instead:

```
# zen_sort_stderr.py
import sys

print("DEBUG >>> About to print the Zen of Python", file=sys.stderr)
import this
print("DEBUG >>> Done printing the Zen of Python", file=sys.stderr)
```

Now, the traces are displayed to the terminal, but they aren’t used as input for the sort command.

### Custom Parsers

You can implement seq by relying on a regular expression if the arguments aren’t too complex. Nevertheless, the regex pattern may quickly render the maintenance of the script difficult. Before you try getting help from specific libraries, another approach is to create a custom parser. The parser is a loop that fetches each argument one after another and applies a custom logic based on the semantics of your program.

```
# seq_parse.py

from typing import Dict, List, Tuple
import collections
import re
import sys

USAGE = (f"Usage: {sys.argv[0]} "
         "[--help] | [-s <sep>] [first [incr]] last")

def seq(operands: List[int], sep: str = "\n") -> str:
    first, increment, last = 1, 1, 1
    if len(operands) == 1:
        last = operands[0]
    if len(operands) == 2:
        first, last = operands
        if first > last:
            increment = -1
    if len(operands) == 3:
        first, increment, last = operands
    last = last + 1 if increment > 0 else last - 1
    return sep.join(str(i) for i in range(first, last, increment))

def parse(args: List[str]) -> Tuple[str, List[int]]:
    arguments = collections.deque(args)
    separator = "\n"
    operands: List[int] = []
    while arguments:
        arg = arguments.popleft()
        if not len(operands):
            if arg == "--help":
                print(USAGE)
                sys.exit(0)
            if arg in ("-s", "--separator"):
                separator = arguments.popleft() if arguments else None
                continue
        try:
            operands.append(int(arg))
        except ValueError:
            raise SystemExit(USAGE)
        if len(operands) > 3:
            raise SystemExit(USAGE)

    return separator, operands

def main() -> None:
    sep, operands = parse(sys.argv[1:])
    if not operands:
        raise SystemExit(USAGE)
    print(seq(operands, sep))

if __name__ == "__main__":
    main()
```

Note that some error handling aspects are kept to a minimum so as to keep the examples relatively short.

This manual approach of parsing the Python command-line arguments may be sufficient for a simple set of arguments. However, it becomes quickly error-prone when complexity increases due to the following:

- A large number of arguments
- Complexity and interdependency between arguments
- Validation to perform against the arguments

The custom approach isn’t reusable and requires reinventing the wheel in each program.

## A Few Methods for Validating Python Command-Line Arguments

You’ve already performed validation for Python command-line arguments in a few examples like seq_regex.py and seq_parse.py.

### Type Validation With Python Data Classes

The following is a proof of concept that attempts to validate the type of the arguments passed at the command line. In the following example, you validate the number of arguments and their respective type:

```
# val_type_dc.py

import dataclasses
import sys
from typing import List, Any

USAGE = f"Usage: python {sys.argv[0]} [--help] | firstname lastname age]"

@dataclasses.dataclass
class Arguments:
    firstname: str
    lastname: str
    age: int = 0

def check_type(obj):
    for field in dataclasses.fields(obj):
        value = getattr(obj, field.name)
        print(
            f"Value: {value}, "
            f"Expected type {field.type} for {field.name}, "
            f"got {type(value)}"
        )
        if type(value) != field.type:
            print("Type Error")
        else:
            print("Type Ok")

def validate(args: List[str]):
    # If passed to the command line, need to convert
    # the optional 3rd argument from string to int
    if len(args) > 2 and args[2].isdigit():
        args[2] = int(args[2])
    try:
        arguments = Arguments(*args)
    except TypeError:
        raise SystemExit(USAGE)
    check_type(arguments)

def main() -> None:
    args = sys.argv[1:]
    if not args:
        raise SystemExit(USAGE)

    if args[0] == "--help":
        print(USAGE)
    else:
        validate(args)

if __name__ == "__main__":
    main()
```

Unless you pass the --help option at the command line, this script expects two or three arguments:

1. A mandatory string: firstname
2. A mandatory string: lastname
3. An optional integer: age

Because all the items in sys.argv are strings, you need to convert the optional third argument to an integer if it’s composed of digits. str.isdigit() validates if all the characters in a string are digits. In addition, by constructing the data class Arguments with the values of the converted arguments, you obtain two validations:

1. If the number of arguments doesn’t correspond to the number of mandatory fields expected by Arguments, then you get an error. This is a minimum of two and a maximum of three fields.
2. If the types after conversion aren’t matching the types defined in the Arguments data class definition, then you get an error.

You can see this in action with the following execution:

```
$ python val_type_dc.py Guido "Van Rossum" 25
Value: Guido, Expected type <class 'str'> for firstname, got <class 'str'>
Type Ok
Value: Van Rossum, Expected type <class 'str'> for lastname, got <class 'str'>
Type Ok
Value: 25, Expected type <class 'int'> for age, got <class 'int'>
Type Ok
```

Similarly, you could also use a NamedTuple to achieve a similar validation.

### Custom Validation

Not unlike what you’ve already explored earlier, detailed validation may require some custom approaches. For example, if you attempt to execute sha1sum_stdin.py with an incorrect file name as an argument, then you get the following:

```
$ python sha1sum_stdin.py bad_file.txt
Traceback (most recent call last):
  ...
FileNotFoundError: [Errno 2] No such file or directory: 'bad_file.txt'
```

bad_file.txt doesn’t exist, but the program attempts to read it.

Revisit main() in sha1sum_stdin.py to handle non-existing files passed at the command line:

```
# sha1sum_val.py

from typing import List
import hashlib
import pathlib
import sys

def process_file(filename: str) -> bytes:
    return pathlib.Path(filename).read_bytes()

def process_stdin() -> bytes:
    return bytes("".join(sys.stdin), "utf-8")

def sha1sum(data: bytes) -> str:
    m = hashlib.sha1()
    m.update(data)
    return m.hexdigest()

def output_sha1sum(data: bytes, filename: str = "-") -> None:
    print(f"{sha1sum(data)}  {filename}")

def main(args: List[str]) -> None:
    if not args:
        output_sha1sum(process_stdin())
    for arg in args:
        if arg == "-":
            output_sha1sum(process_stdin(), "-")
            continue
        try:
            output_sha1sum(process_file(arg), arg)
        except (FileNotFoundError, IsADirectoryError) as err:
            print(f"{sys.argv[0]}: {arg}: {err.strerror}", file=sys.stderr)

if __name__ == "__main__":
    main(sys.argv[1:])
```

When you execute this modified script, you get this:

```
$ python sha1sum_val.py bad_file.txt
sha1sum_val.py: bad_file.txt: No such file or directory
```

Note that the error displayed to the terminal is written to stderr, so it doesn’t interfere with the data expected by a command that would read the output of sha1sum_val.py:

```
$ python sha1sum_val.py bad_file.txt main.py | cut -d " " -f 1
sha1sum_val.py: bad_file.txt: No such file or directory
d84372fc77a90336b6bb7c5e959bcb1b24c608b4
```

## The Python Standard Library

Despite the different approaches you took to process Python command-line arguments, any complex program might be better off leveraging existing libraries to handle the heavy lifting required by sophisticated command-line interfaces. As of Python 3.7, there are three command line parsers in the standard library:

1. argparse
2. getopt
3. optparse

The recommended module to use from the standard library is argparse. The standard library also exposes optparse but it’s officially deprecated and only mentioned here for your information. It was superseded by argparse in Python 3.2 and you won’t see it discussed in this tutorial.

### argparse

You’re going to revisit sha1sum_val.py, the most recent clone of sha1sum, to introduce the benefits of argparse. To this effect, you’ll modify main() and add init_argparse to instantiate argparse.ArgumentParser:

```
import argparse

def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        usage="%(prog)s [OPTION] [FILE]...",
        description="Print or check SHA1 (160-bit) checksums."
    )
    parser.add_argument(
        "-v", "--version", action="version",
        version = f"{parser.prog} version 1.0.0"
    )
    parser.add_argument('files', nargs='*')
    return parser

def main() -> None:
    parser = init_argparse()
    args = parser.parse_args()
    if not args.files:
        output_sha1sum(process_stdin())
    for file in args.files:
        if file == "-":
            output_sha1sum(process_stdin(), "-")
            continue
        try:
            output_sha1sum(process_file(file), file)
        except (FileNotFoundError, IsADirectoryError) as err:
            print(f"{sys.argv[0]}: {file}: {err.strerror}", file=sys.stderr)
```

For the cost of a few more lines compared to the previous implementation, you get a clean approach to add --help and --version options that didn’t exist before. The expected arguments (the files to be processed) are all available in field files of object argparse.Namespace. This object is populated on line 17 by calling parse_args().

To illustrate the immediate benefit you obtain by introducing argparse in this program, execute the following:

```
$ python sha1sum_argparse.py --help
usage: sha1sum_argparse.py [OPTION] [FILE]...

Print or check SHA1 (160-bit) checksums.

positional arguments:
  files

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  show program's version number and exit
```

To delve into the details of argparse, check out Build Command-Line Interfaces With Python's argparse.

### getopt

getopt finds its origins in the getopt C function. It facilitates parsing the command line and handling options, option arguments, and arguments. Revisit parse from seq_parse.py to use getopt:

```
def parse():
    options, arguments = getopt.getopt(
        sys.argv[1:],                      # Arguments
        'vhs:',                            # Short option definitions
        ["version", "help", "separator="]) # Long option definitions
    separator = "\n"
    for o, a in options:
        if o in ("-v", "--version"):
            print(VERSION)
            sys.exit()
        if o in ("-h", "--help"):
            print(USAGE)
            sys.exit()
        if o in ("-s", "--separator"):
            separator = a
    if not arguments or len(arguments) > 3:
        raise SystemExit(USAGE)
    try:
        operands = [int(arg) for arg in arguments]
    except ValueError:
        raise SystemExit(USAGE)
    return separator, operands
```

getopt.getopt() takes the following arguments:

1. The usual arguments list minus the script name, sys.argv[1:]
2. A string defining the short options
3. A list of strings for the long options

Note that a short option followed by a colon (:) expects an option argument, and that a long option trailed with an equals sign (=) expects an option argument.

## A Few External Python Packages

Building upon the existing conventions you saw in this tutorial, there are a few libraries available on the Python Package Index (PyPI) that take many more steps to facilitate the implementation and maintenance of command-line interfaces.

### Click

As of this writing, Click is perhaps the most advanced library to build a sophisticated command-line interface for a Python program. It’s used by several Python products, most notably Flask and Black.

To install Click, proceed as follows:

```
$ python -m pip install click
```

So, how could Click help you handle the Python command-line arguments? Here’s a variation of the seq program using Click:

```
# seq_click.py

import click

@click.command(context_settings=dict(ignore_unknown_options=True))
@click.option("--separator", "-s",
              default="\n",
              help="Text used to separate numbers (default: \\n)")
@click.version_option(version="1.0.0")
@click.argument("operands", type=click.INT, nargs=-1)
def seq(operands, separator) -> str:
    first, increment, last = 1, 1, 1
    if len(operands) == 1:
        last = operands[0]
    elif len(operands) == 2:
        first, last = operands
        if first > last:
            increment = -1
    elif len(operands) == 3:
        first, increment, last = operands
    else:
        raise click.BadParameter("Invalid number of arguments")
    last = last - 1 if first > last else last + 1
    print(separator.join(str(i) for i in range(first, last, increment)))

if __name__ == "__main__":
    seq()
```

Setting ignore_unknown_options to True ensures that Click doesn’t parse negative arguments as options. Negative integers are valid seq arguments.

As you may have observed, you get a lot for free! A few well-carved decorators are sufficient to bury the boilerplate code, allowing you to focus on the main code, which is the content of seq() in this example.

Click offers many niceties that will help you craft a very professional command-line interface:

- Output coloring
- Prompt for omitted arguments
- Commands and sub-commands
- Argument type validation
- Callback on options and arguments
- File path validation
- Progress bar

### Python Prompt Toolkit

There are other popular Python packages that are handling the command-line interface problem, like docopt for Python. So, you may find the choice of the Prompt Toolkit a bit counterintuitive.

The Python Prompt Toolkit provides features that may make your command line application drift away from the Unix philosophy. However, it helps to bridge the gap between an arcane command-line interface and a full-fledged graphical user interface. In other words, it may help to make your tools and programs more user-friendly.

You can use this tool in addition to processing Python command-line arguments as in the previous examples, but this gives you a path to a UI-like approach without you having to depend on a full Python UI toolkit. To use prompt_toolkit, you need to install it with pip:

```
$ python -m pip install prompt_toolkit
```

## Conclusion

In this tutorial, you’ve navigated many different aspects of Python command-line arguments. You should feel prepared to apply the following skills to your code:

- The conventions and pseudo-standards of Python command-line arguments
- The origins of sys.argv in Python
- The usage of sys.argv to provide flexibility in running your Python programs
- The Python standard libraries like argparse or getopt that abstract command line processing
- The powerful Python packages like click and prompt_toolkit to further improve the usability of your programs

Whether you’re running a small script or a complex text-based application, when you expose a command-line interface you’ll significantly improve the user experience of your Python software.

Next time you use your application, you’ll appreciate the documentation you supplied with the --help option or the fact that you can pass options and arguments instead of modifying the source code to supply different data.

## Additional Resources

To gain further insights about Python command-line arguments and their many facets, you may want to check out the following resources:

- Comparing Python Command-Line Parsing Libraries – Argparse, Docopt, and Click
- Python, Ruby, and Golang: A Command-Line Application Comparison

You may also want to try other Python libraries that target the same problems while providing you with different solutions:

- Typer
- Plac
- Cliff
- Cement
- Python Fire
