def search(lst, key):

    assert monotonic(lst), "The list is not sorted"

    low = 0
    mid = len(lst) // 2
    high = len(lst) - 1

    while (high >= low):
        mid = (high + low) // 2
        if (lst[mid] < key):
          low = mid + 1
        elif (lst[mid] > key):
            high = mid - 1
        else:
            return mid

    return -1