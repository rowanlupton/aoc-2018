from typing import List


def first_frequency_reached_twice(
    changes: List[str],
    initial_value: int = 0
) -> int:
    value = initial_value
    frequencies_reached = []

    i = 0
    while value not in frequencies_reached:
        # Add the new frequency to the list of frequencies seen
        frequencies_reached.append(value)

        change = changes[i % len(changes)]

        # Update the frequency
        if change[0] == '-':
            value = value - int(change[1:])
        else:
            value = value + int(change[1:])

        print('{}: {}'.format(i, value))

        i += 1

    return value


if __name__ == '__main__':
    with open('data/1.txt', 'r') as file:
        print(
            first_frequency_reached_twice(
                [x.strip() for x in file.readlines()]
            )
        )
