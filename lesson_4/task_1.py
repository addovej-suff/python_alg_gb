# Проанализировать скорость и сложность одного любого алгоритма
# из разработанных в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать,
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл
# с кодом (не забудьте указать, для каких N вы проводили замеры),
# ● написать общий вывод: какой из трёх вариантов лучше и почему.

# В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from cProfile import run as c_run
from timeit import timeit
from random import randint

from matplotlib import pyplot as plt


def test(func):
    print(f'Test function \x1b[1;37;33m{func.__name__}\x1b[0m', end=' ')

    _sum, array = func()

    idx_min = 0
    idx_max = 0
    for i in range(1, len(array)):
        if array[i] < array[idx_min]:
            idx_min = i
        elif array[i] > array[idx_max]:
            idx_max = i

    if idx_min > idx_max:
        idx_min, idx_max = idx_max, idx_min

    test_sum = 0
    for i in range(idx_min + 1, idx_max):
        test_sum += array[i]

    assert _sum == test_sum, f'{_sum} != {test_sum}'
    print('OK')


def first(size=20, min_item=1, max_item=99):
    array = [randint(min_item, max_item) for _ in range(size)]

    extremum = {
        'max': (0, array[0]),
        'min': (0, array[0])
    }

    for i, val in enumerate(array):
        if val > extremum['max'][1]:
            extremum['max'] = (i, val)

        if val < extremum['min'][1]:
            extremum['min'] = (i, val)

    if extremum['max'][0] < extremum['min'][0]:
        start = extremum['max'][0] + 1
        end = extremum['min'][0]
    else:
        start = extremum['min'][0] + 1
        end = extremum['max'][0]

    _sum = 0
    for i in array[start: end]:
        _sum += i

    return _sum, array


def second(size=20, min_item=1, max_item=99):
    array = [randint(min_item, max_item) for _ in range(size)]

    idx_min = 0
    idx_max = 0
    for i in range(1, len(array)):
        if array[i] < array[idx_min]:
            idx_min = i
        elif array[i] > array[idx_max]:
            idx_max = i

    if idx_min > idx_max:
        idx_min, idx_max = idx_max, idx_min

    _sum = 0
    for i in range(idx_min + 1, idx_max):
        _sum += array[i]

    return _sum, array


def third(size=20, min_item=1, max_item=99):
    array = [randint(min_item, max_item) for _ in range(size)]

    _max = max(array)
    _min = min(array)

    start = array.index(_min)
    end = array.index(_max)

    if end < start:
        end, start = start, end

    _sum = sum(array[start + 1: end])
    return _sum, array


def plot_timeit(timeit_count=1000):
    sizes = []
    first_times = []
    second_times = []
    third_times = []
    _start = 20
    _end = 30000
    _step = 500
    for size in range(_start, _end, _step):
        print(f'Calculating {size}-size of array')
        sizes.append(size)
        first_times.append(timeit(f'first({size})', number=timeit_count, globals=globals()))
        second_times.append(timeit(f'second({size})', number=timeit_count, globals=globals()))
        third_times.append(timeit(f'third({size})', number=timeit_count, globals=globals()))

    plt.plot(sizes, first_times, 'r')  # Red
    plt.plot(sizes, second_times, 'b')  # Blue
    plt.plot(sizes, third_times, 'y')  # Yellow
    plt.title(
        f'Timeit count: {timeit_count}, Array sizes from {_start} to {_end} with {_step} step')
    plt.xlabel('N')  # N-size of array
    plt.ylabel('T')  # Time
    plt.grid()
    plt.show()


if __name__ == '__main__':
    # Все замеры были сделаны на машине:
    # OS macOS High Sierra
    # 3 GHz Intel Core i5 (7400)
    # 24 GB 2400 MHz DDR4

    test(first)
    test(second)
    test(third)

    plot_timeit()

    c_run('first(1000)')
    #       5323 function calls in 0.002 seconds
    #
    # Ordered by: standard name
    #
    # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    #      1    0.000    0.000    0.002    0.002 <string>:1(<module>)
    #   1000    0.001    0.000    0.001    0.000 random.py:174(randrange)
    #   1000    0.000    0.000    0.002    0.000 random.py:218(randint)
    #   1000    0.001    0.000    0.001    0.000 random.py:224(_randbelow)
    #      1    0.000    0.000    0.002    0.002 task_1.py:46(first)
    #      1    0.000    0.000    0.002    0.002 task_1.py:47(<listcomp>)
    #      1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
    #   1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
    #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    #   1318    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

    c_run('second(1000)')
    #       5345 function calls in 0.002 seconds
    #
    # Ordered by: standard name
    #
    # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    #      1    0.000    0.000    0.002    0.002 <string>:1(<module>)
    #   1000    0.001    0.000    0.001    0.000 random.py:174(randrange)
    #   1000    0.000    0.000    0.002    0.000 random.py:218(randint)
    #   1000    0.001    0.000    0.001    0.000 random.py:224(_randbelow)
    #      1    0.000    0.000    0.002    0.002 task_1.py:75(second)
    #      1    0.000    0.000    0.002    0.002 task_1.py:76(<listcomp>)
    #      1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
    #      1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
    #   1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
    #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    #   1339    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

    c_run('third(1000)')
    #       5312 function calls in 0.002 seconds
    #
    # Ordered by: standard name
    #
    # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    #      1    0.000    0.000    0.002    0.002 <string>:1(<module>)
    #   1000    0.001    0.000    0.001    0.000 random.py:174(randrange)
    #   1000    0.000    0.000    0.002    0.000 random.py:218(randint)
    #   1000    0.001    0.000    0.001    0.000 random.py:224(_randbelow)
    #      1    0.000    0.000    0.002    0.002 task_1.py:96(third)
    #      1    0.000    0.000    0.002    0.002 task_1.py:97(<listcomp>)
    #      1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
    #      1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
    #      1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
    #      1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
    #   1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
    #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    #   1302    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
    #      2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

    # Заключение:
    # Время выполнения алгоритма линейно, но прыгает из-за рандома.
    # Первые два примерно одинаковы по времени выполнения
    # Третий алгоритм является наиболее быстрым за счет использования встроенных функций.
    # Первые два алгоритма выиграли только в одной точке при N = 8000,
    # можно считать это погрешностью
