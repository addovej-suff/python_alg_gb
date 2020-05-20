# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.


from random import randint


SIZE = 20
MIN_ITEM = 1
MAX_ITEM = 99

array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(*array, sep=', ')

# Store here max and min values with indexes
extremum = {
    'max': (0, array[0]),
    'min': (0, array[0])
}

for i, val in enumerate(array):
    if val > extremum['max'][1]:
        extremum['max'] = (i, val)

    if val < extremum['min'][1]:
        extremum['min'] = (i, val)

print(f'Max: {extremum["max"]}, Min: {extremum["min"]}')

# Swap max with min values
array[extremum['max'][0]], array[extremum['min'][0]] = array[extremum['min'][0]], array[extremum['max'][0]]
print(*array, sep=', ')
