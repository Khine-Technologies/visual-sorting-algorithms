import random


def make_array(arr_len: int, low: int, high: int) -> list[int]:
    arr = []
    for i in range(arr_len):
        arr.append(random.randint(low, high))

    return arr


def swap(arr: list[int], x: int, y: int) -> None:
    arr[x], arr[y] = arr[y], arr[x]
