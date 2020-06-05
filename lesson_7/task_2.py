# Отсортируйте по возрастанию методом слияния одномерный вещественный
# массив, заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

from random import uniform

from tests import test_sort


def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    new_arr = []
    idx_l = 0
    idx_r = 0

    for _ in range(len(left) + len(right)):
        if idx_l < len(left) and idx_r < len(right):
            if left[idx_l] <= right[idx_r]:
                new_arr.append(left[idx_l])
                idx_l += 1
            else:
                new_arr.append(right[idx_r])
                idx_r += 1
        elif len(left) == idx_l:
            new_arr.append(right[idx_r])
            idx_r += 1
        elif len(right) == idx_r:
            new_arr.append(left[idx_l])
            idx_l += 1

    return new_arr


MIN = 0
MAX = 49.99
DEC_PLACES = 2
SIZE = 10
array = [round(uniform(MIN, MAX), DEC_PLACES) for i in range(SIZE)]

# Test sort function
test_sort(merge_sort, array.copy())

print(array)
print(merge_sort(array))
