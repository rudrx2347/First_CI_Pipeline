"""Program 26: Calculate the sum without using sum()."""

def sum_of_list(numbers):
    total = 0

    for number in numbers:
        total += number

    return total
