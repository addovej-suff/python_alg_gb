# Массив размером 2m + 1, где m — натуральное число, заполнен
# случайным образом. Найдите в массиве медиану. Медианой называется
# элемент ряда, делящий его на две равные части: в одной находятся
# элементы, которые не меньше медианы, в другой — не больше медианы.

from random import randint

from tests import test_median


def median_search(arr, mid=None):
    if len(arr) == 1:
        return arr[0]

    if mid is None:
        mid = len(array) / 2
    support_el = arr[randint(0, len(arr) - 1)]

    left_buff = []
    right_buff = []
    supports = []
    for i in arr:
        if i < support_el:
            left_buff.append(i)
        elif i > support_el:
            right_buff.append(i)
        else:
            supports.append(i)

    if mid < len(left_buff):
        return median_search(left_buff, mid)
    elif mid < len(left_buff) + len(supports):
        return supports[0]
    else:
        return median_search(right_buff, mid - len(left_buff) - len(supports))


M = 10
SIZE = 2 * M + 1
MIN = 1
MAX = 20

array = [randint(MIN, MAX) for _ in range(SIZE)]

# Test median search function
test_median(median_search, array.copy())

print(array)
print(f'Медиана: {median_search(array)}')
