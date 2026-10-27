"""Program 25: Find maximum and minimum without max() or min()."""

def find_max_min(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")

    maximum = numbers[0]
    minimum = numbers[0]

    for number in numbers[1:]:
        if number > maximum:
            maximum = number
        if number < minimum:
            minimum = number

    return maximum, minimum
