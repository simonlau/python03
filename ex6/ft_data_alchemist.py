#!/usr/bin/env python3

import random
from typing import TypeAlias

Player: TypeAlias = str
Score: TypeAlias = int


def main() -> None:
    print("=== Inventory System Analysis ==")
    players: list[Player] = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kelvin",
        "Liam",
    ]
    print(f"Initial list of players: {players}")

    all_caps: list[Player] = [p.capitalize() for p in players]
    print(f"New list with all names capitalized: {all_caps}")

    only_caps: list[Player] = [p for p in players if p[0].isupper()]
    print(f"New list of capitalized names only: {only_caps}")

    score_dict: dict[Player, Score] = {
        # ruff:ignore[suspicious-non-cryptographic-random-usage]
        p: random.randint(0, 1000)
        for p in all_caps
    }
    print(f"Score dict: {score_dict}")

    average = sum(score_dict.values()) / len(score_dict)
    print(f"Score average is {round(average, 2)}")

    high_scores: dict[Player, Score] = {
        name: score for name, score in score_dict.items() if score > average
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
