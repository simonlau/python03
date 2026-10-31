#!/usr/bin/env python3

from collections.abc import Iterator
from collections.abc import Generator
from typing import TypeAlias
import random

Name: TypeAlias = str
Action: TypeAlias = str
Event: TypeAlias = tuple[Name, Action]

actions: list[Action] = ["run", "eat", "sleep", "grab", "move", "climb", "swim"]
names: list[Name] = ["alice", "bob", "charlie", "dylan"]


def gen_event() -> Generator[Event, None, None]:
    while True:
        action = random.choice(actions)
        name = random.choice(names)
        yield name, action


def consume_event(events: list[Event]) -> Iterator[Event]:
    while True:
        index = random.randint(0, len(events) - 1)
        event = events.pop(index)
        yield event
        if len(events) == 0:
            return


def main() -> None:
    print("=== Game Data Stream Processor ==")
    i = 0
    event_generator = gen_event()
    while i < 1000:
        name, action = next(event_generator)
        print(f"Event {i}: Player {name} did action {action}")
        i += 1

    i = 0
    num = 10
    events: list[Event] = []
    while i < num:
        events.append(next(event_generator))
        i += 1
    print(f"Built list of {num} events: {events}")
    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()
