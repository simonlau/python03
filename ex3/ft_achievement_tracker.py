#!/usr/bin/env python3

import random
from typing import Literal, TypeAlias

Achievement: TypeAlias = Literal[
    "Crafting Genius",
    "Strategist",
    "World Savior",
    "Speed Runner",
    "Survivor",
    "Master Explorer",
    "Treasure Hunter",
    "Unstoppable",
    "First Steps",
    "Collector Supreme",
    "Untouchable",
    "Sharp Mind",
    "Boss Slayer",
]


def gen_player_achievements(
    achievements: list[Achievement],
) -> set[Achievement]:
    # ruff:ignore[suspicious-non-cryptographic-random-usage]
    count = random.randint(4, len(achievements))
    return set(random.sample(achievements, count))


def main() -> None:
    achievements: list[Achievement] = [
        "Crafting Genius",
        "Strategist",
        "World Savior",
        "Speed Runner",
        "Survivor",
        "Master Explorer",
        "Treasure Hunter",
        "Unstoppable",
        "First Steps",
        "Collector Supreme",
        "Untouchable",
        "Sharp Mind",
        "Boss Slayer",
    ]
    print("=== Achievement Tracker System ===\n")

    alice: set[Achievement] = gen_player_achievements(achievements)
    bob: set[Achievement] = gen_player_achievements(achievements)
    charlie: set[Achievement] = gen_player_achievements(achievements)
    dylan: set[Achievement] = gen_player_achievements(achievements)

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    print(f"\nAll distinct achievements: {alice | bob | charlie | dylan}\n")

    print(f"Common achievements: {alice & bob & charlie & dylan}\n")

    print(f"Only Alice has: {alice - bob - charlie - dylan}")
    print(f"Only Bob has: {bob - alice - charlie - dylan}")
    print(f"Only Charlie has: {charlie - alice - bob - dylan}")
    print(f"Only Dylan has: {dylan - alice - bob - charlie}")
    print()

    print(f"Alice is missing: {set(achievements) - alice}")
    print(f"Bob is missing: {set(achievements) - bob}")
    print(f"Charlie is missing: {set(achievements) - charlie}")
    print(f"Dylan is missing: {set(achievements) - dylan}")


if __name__ == "__main__":
    main()
