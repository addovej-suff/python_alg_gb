# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход
# натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
#
# Первый — с помощью алгоритма «Решето Эратосфена».
# Второй — без использования «Решета Эратосфена».

from itertools import count as icount
from itertools import islice
from cProfile import run as c_run
from timeit import timeit

from matplotlib import pyplot as plt


def test(func):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]

    print(f'Test function \x1b[1;37;33m{func.__name__}\x1b[0m')
    print(f'Tests count: {len(primes)}')

    for i, val in enumerate(primes, start=1):
        res = func(i)
        assert res == val, f'{res} != {val}'

        print('OK', end=' ')
    print()


def sieve(n):
    """
    :param n: int
        1 < n < 78498
    :return: int
        prime number
    """

    assert 0 < n < 78498, 'Необходимо ввести номер простого числа от 1 до 78497'

    init_num = 1000000
    _sieve = [i for i in range(init_num)]
    _sieve[1] = 0

    for i in range(2, init_num):
        if _sieve[i] != 0:
            j = i + i
            while j < init_num:
                _sieve[j] = 0
                j += i

    res = [i for i in _sieve if i != 0]
    return res[n - 1]


def prime(n):
    def _primes():
        yield 2

        for num in icount(3, 2):
            d = 3
            while d * d <= num and num % d != 0:
                d += 2
            if d * d > num:
                yield num

    return next(islice(_primes(), n - 1, None))


def plot_timeit():
    cases = []
    sieve_times = []
    prime_times = []
    timeit_count = 1000
    _end = 10000
    _step = 499
    for case in range(1, _end, _step):
        print(f'Calculating {case}-i prime number')
        cases.append(case)
        sieve_times.append(timeit(f'sieve({case})', number=timeit_count, globals=globals()))
        prime_times.append(timeit(f'prime({case})', number=timeit_count, globals=globals()))

    plt.plot(cases, sieve_times, 'r')
    plt.plot(cases, prime_times, 'b')
    plt.title(f'Timeit count: {timeit_count}, Max: {_end}, Step: {_step}')
    plt.xlabel('N')  # N-i prime number
    plt.ylabel('T')  # Time
    plt.grid()
    plt.show()


# test(sieve)
# test(prime)

# plot_timeit()

c_run('sieve(10000)')
c_run('prime(10000)')


# Анализ:
# Алгоритм «Решето Эратосфена» подразумевает исключение не простых чисел из какого-то массива.
# Для нахождения N-го простого числа, требуется исходный массив чисел такого размера,
# чтобы получившийся массив простых чисел был размером не меньше N.
# В ходе оптимизации не был найден способ, который позволил бы динамически формировать исходный массив,
# размер которого зависел бы от N согласно условию выше.
# Текущая реализация алгоритма имеет сложность

# Второй алгоритм будет иметь сложность O(N/2)...

# Заключение:
