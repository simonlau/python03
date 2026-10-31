#!/usr/bin/env python3

from typing import TypeAlias
import math

Coordinate: TypeAlias = tuple[float, float, float]


def str_to_float(s: str) -> float | None:
    try:
        f = float(s)
        return f
    except ValueError:
        print(f"Error on parameter {s}: could not convert string to float {s}")
    return None


def get_player_pos() -> Coordinate:
    keep_asking = True
    input_list: list[float] = []
    while keep_asking:
        enter_msg = "Enter new coordinates as floats in format 'x,y,z': "
        input_coordinates = input(enter_msg)
        input_list = [
            f
            for s in input_coordinates.split(",")
            if (f := str_to_float(s)) is not None
        ]
        match input_list:
            case [_, _, _]:
                keep_asking = False
            case _:
                print("Invalid syntax")
    x, y, z = input_list
    return x, y, z


def calc_distance(one: Coordinate, two: Coordinate) -> float:
    x1, y1, z1 = one
    x2, y2, z2 = two
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def main() -> None:
    print("=== Game Coordinate System ==")
    print("Get a first set of coordinates")
    first = get_player_pos()
    print(f"Got a first tuple: {first}")
    x1, y1, z1 = first
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    distance = calc_distance((x1, y1, z1), (0, 0, 0))
    print(f"Distance to center: {round(distance, 4)}\n")

    print("Get a second set of coordinates")
    second = get_player_pos()
    distance = calc_distance(second, (x1, y1, z1))
    print(f"Distance between the 2 sets of coordinates: {round(distance, 4)}")


if __name__ == "__main__":
    main()
