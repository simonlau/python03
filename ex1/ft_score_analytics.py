#!/usr/bin/env python3

import sys
from typing import TypeAlias

Score: TypeAlias = int


def str_to_score(s: str) -> Score | None:
    try:
        num = int(s)
    except ValueError:
        print(f"Invalid parameter: '{s}'")
        return None
    else:
        return num


def main() -> None:
    print("=== Player Score Analytics ==")
    args = sys.argv[1:]
    if len(args) == 0:
        print("No scores provided. ", end="")
        print("Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return

    scores: list[Score] = [
        result for x in args if (result := str_to_score(x)) is not None
    ]

    if len(scores) == 0:
        print("No scores provided. ", end="")
        print("Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return

    total = sum(scores)
    num = len(scores)
    high = max(scores)
    low = min(scores)
    print(f"Scores processed: {scores}")
    print(f"Total players: {num}")
    print(f"Total score: {total}")
    print(f"Average score: {total / num:.1f}")
    print(f"High score: {high}")
    print(f"Low score: {low}")
    print(f"Score range: {high - low}")


if __name__ == "__main__":
    main()
