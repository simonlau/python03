#!/usr/bin/env python3

import sys


def main():
    print("=== Command Quest ==")
    total = len(sys.argv) - 1
    if total == 0:
        print("No arguments provided!")
        print(f"Total arguments: {total + 1}")
        return
    i = 0
    print(f"Arguments received: {total}")
    while (i <= total):
        print(f"Argument {i}: {sys.argv[i]}")
        i += 1
    print(f"Total arguments: {total + 1}")


if __name__ == '__main__':
    main()
