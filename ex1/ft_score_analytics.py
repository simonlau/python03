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
    print("=== Play Score Analytics ==")
    total = len(sys.argv) - 1
    if total == 0:
        print("No scores provided. ", end="")
        print("Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return

    scores: list[Score] = [
        result for x in sys.argv[1:] if (result := str_to_score(x)) is not None
    ]
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()
