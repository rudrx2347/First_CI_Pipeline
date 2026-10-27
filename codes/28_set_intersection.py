"""Program 28: Find the intersection of two sets."""

def set_intersection(first, second):
    result = set()

    for item in first:
        if item in second:
            result.add(item)

    return result
