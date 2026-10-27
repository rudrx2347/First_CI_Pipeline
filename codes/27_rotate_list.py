"""Program 27: Rotate a list by k positions."""

def rotate_list(items, k):
    if not items:
        return []

    k = k % len(items)
    return items[-k:] + items[:-k] if k else items.copy()
