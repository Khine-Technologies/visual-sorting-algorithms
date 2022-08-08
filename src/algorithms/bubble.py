import os
import time


def sort(arr: list[int], ani_delay: float):
    arr_len = len(arr)
    print(arr)
    for i in range(arr_len):
        for j in range(arr_len-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            os.system('clear')
            print(arr)
            time.sleep(ani_delay)
