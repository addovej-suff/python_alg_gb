# Отсортируйте по убыванию методом пузырька одномерный
# целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# ● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# ● постарайтесь сделать алгоритм умнее, но помните, что у вас
#   должна остаться сортировка пузырьком. Улучшенные версии сортировки,
#   например, расчёской, шейкерная и другие в зачёт не идут.

from random import randint

from tests import test_sort


def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


SIZE = 15
MIN = -100
MAX = 99
array = [randint(MIN, MAX) for i in range(SIZE)]

# Test sort function
test_sort(bubble_sort, array.copy(), True)

print(array)
print(bubble_sort(array))
