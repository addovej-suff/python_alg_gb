# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.


from random import randint


SIZE = 20
MIN_ITEM = -20
MAX_ITEM = 20

array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(*array, sep=', ')

max_negative = None

# Checking all negative items and store max
for i, val in enumerate(array):
    if max_negative is None:
        if val < 0:
            max_negative = (i, val)
    elif max_negative[1] < val < 0:
        max_negative = (i, val)

if max_negative is None:
    print('Отрицательных элементов нет в списке')
else:
    print(*max_negative, sep=': ')
