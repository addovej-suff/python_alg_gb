# В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.


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

# Determining start and end bounds
if extremum['max'][0] < extremum['min'][0]:
    start = extremum['max'][0] + 1
    end = extremum['min'][0]
else:
    start = extremum['min'][0] + 1
    end = extremum['max'][0]

sum_ = 0
for i in array[start: end]:
    sum_ += i

print(f'Сумма: {sum_}')
