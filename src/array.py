import random


def make(arr_len: int, low: int, high: int) -> list[int]:
    arr = []
    for i in range(arr_len):
        arr.append(random.randint(low, high))

    return arr
