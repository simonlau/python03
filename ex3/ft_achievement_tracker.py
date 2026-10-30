#!/usr/bin/env python3

import random


def gen_player_achievements(achievements: list[str]):
    num = random.randint(3, len(achievements) + 3)
    i = 0
    result = set()
    while (i < num):
        result.add(random.choice(achievements))
        i += 1
    return result


def main():
    achievements = ['Crafting Genius',
                    'Strategist',
                    'World Savior',
                    'Speed Runner',
                    'Survivor',
                    'Master Explorer',
                    'Treasure Hunter',
                    'Unstoppable',
                    'First Steps',
                    'Collector Supreme',
                    'Untouchable',
                    'Sharp Mind',
                    'Boss Slayer']
    print("=== Achievement Tracker System ==\n")

    alice = gen_player_achievements(achievements)
    bob = gen_player_achievements(achievements)
    charlie = gen_player_achievements(achievements)
    dylan = gen_player_achievements(achievements)

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    print(f"All distinct achievements: {achievements}")

    print(f"Common achievements: {alice & bob & charlie & dylan}\n")

    print(f"Only Alice has: {alice - bob - charlie - dylan}")
    print(f"Only Bob has: {bob - alice - charlie - dylan}")
    print(f"Only Charlie has: {charlie - alice - bob - dylan}")
    print(f"Only Dylan has: {dylan - alice - bob - charlie}")
    print("")

    print(f"Alice is missing: {set(achievements) - alice}")
    print(f"Bob is missing: {set(achievements) - bob}")
    print(f"Charlie is missing: {set(achievements) - charlie}")
    print(f"Dylan is missing: {set(achievements) - dylan}")


if __name__ == '__main__':
    main()
