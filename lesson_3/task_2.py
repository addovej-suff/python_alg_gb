# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.


from random import randint


SIZE = 20
MIN_ITEM = 1
MAX_ITEM = 99

array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(*array, sep=', ')

new_array = [i for i, val in enumerate(array) if val % 2 == 0]
print(*new_array, sep=', ')
