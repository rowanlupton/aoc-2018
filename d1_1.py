from typing import Iterable


def process_frequency_changes(
    changes: Iterable[str],
    initial_value: int = 0
) -> int:
    value = initial_value
    for change in changes:
        if change[0] == '-':
            value = value - int(change[1:])
        else:
            value = value + int(change[1:])
    return value


if __name__ == '__main__':
    with open('data/1.txt', 'r') as file:
        print(process_frequency_changes(x.strip() for x in file.readlines()))
