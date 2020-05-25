def avg(arr):
    s = sum(arr)
    l = len(arr)
    if l <= 0:
        return None
    return s / l


def median_odd(arr):
    l = len(arr)
    m = (l - 1) // 2
    return arr[m]

def median_even(arr):
    l = len(arr)
    n1 = arr[(l // 2) - 1]
    n2 = arr[l // 2]
    m = (n1 + n2) / 2
    return m

def median(ori_arr):
    arr = ori_arr.copy()
    arr.sort()
    l = len(arr)
    if l <= 0:
        return None
    if l % 2 == 1:
        return median_odd(arr)
    else:
        return median_even(arr)
