def second_largest(arr):
    arr_sorted = sorted(set(arr))
    if len(arr_sorted) < 2:
        return None
    return arr_sorted[-2]

def range_diff(arr):
    return max(arr) - min(arr)

def median(arr):
    arr_sorted = sorted(arr)
    n = len(arr_sorted)
    if n % 2 == 1:
        return arr_sorted[n // 2]
    else:
        mid1, mid2 = arr_sorted[n // 2 - 1], arr_sorted[n // 2]
        return (mid1 + mid2) / 2

def smallest_largest(arr):
    return [min(arr), max(arr)]

def array_to_string(arr):
    return '-'.join(map(str, arr))