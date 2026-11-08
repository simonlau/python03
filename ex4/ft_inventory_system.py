#!/usr/bin/env python3

import sys
from typing import TypeAlias

Item: TypeAlias = str
Quantity: TypeAlias = int
Item_Quantity_Pair: TypeAlias = tuple[Item, Quantity]


def int_to_quantity(num: int) -> Quantity:
    if num < 0:
        msg = f"Negative number for quantity: {num}"
        raise ValueError(msg)
    return num


def str_to_tuple(s: str) -> Item_Quantity_Pair | None:
    key: Item = ""
    value: str = ""
    try:
        key, value = s.split(":")
    except ValueError:
        print(f"Error - invalid parameter '{s}'")
        return None
    try:
        quantity = int_to_quantity(int(value))
    except ValueError as error:
        print(f"Quantity error for '{key}': {error}")
        return None
    else:
        return key, quantity


def main() -> None:
    print("=== Inventory System Analysis ==")
    inventory: dict[Item, Quantity] = {}
    items: list[Item_Quantity_Pair] = [
        item_quantity
        for s in sys.argv[1:]
        if (item_quantity := str_to_tuple(s)) is not None
    ]
    for item, quantity in items:
        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
        else:
            inventory[item] = quantity
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")

    total: int = 0
    for quantity in inventory.values():
        total += quantity
    print(f"Total quantity of the {len(inventory)} items: {total}")

    if len(inventory) > 0:
        first_item, first_item_quantity = items[0]
        most: Item_Quantity_Pair = first_item, first_item_quantity
        least: Item_Quantity_Pair = first_item, first_item_quantity
        for item, quantity in inventory.items():
            if quantity > most[1]:
                most = item, quantity
            if quantity < least[1]:
                print(f"least: {item} {quantity}")
                least = item, quantity
            percent = round(quantity / total * 100, 1)
            print(f"Item {item} represents {percent}%")
        print(f"Item most abundant: {most[0]} with quantity {most[1]}")
        print(f"Item least abundant: {least[0]} with quantity {least[1]}")
    else:
        print("Item most abundant: No item")
        print("Item least abundant: No item")
    inventory["magic_item"] = 1
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
