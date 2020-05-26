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
    assert n > 0, 'Необходимо ввести номер простого числа от > 0'

    if n == 1:
        return 2

    chunk_start = 2
    chunk_size = n
    primes_len = 0
    res = [0, 0]

    while primes_len < n:
        _sieve = res + [i for i in range(chunk_start, chunk_size)]
        for i in range(2, chunk_size):
            if _sieve[i] != 0:
                j = i + i
                while j < chunk_size:
                    _sieve[j] = 0
                    j += i

        res = _sieve
        primes_len = len([i for i in _sieve if i != 0])
        chunk_start = chunk_size
        chunk_size = 5 * chunk_size

    res = [i for i in res if i != 0]
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
    assert n > 0, 'Необходимо ввести номер простого числа от > 0'

    return next(islice(_primes(), n - 1, None))


def plot_timeit():
    cases = []
    sieve_times = []
    prime_times = []
    timeit_count = 1000
    _end = 10000
    _step = 500
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


if __name__ == '__main__':
    # Все замеры были сделаны на машине:
    # OS macOS High Sierra
    # 3 GHz Intel Core i5 (7400)
    # 24 GB 2400 MHz DDR4

    test(sieve)
    test(prime)

    plot_timeit()

    c_run('sieve(90000)')
    #           20 function calls in 1.392 seconds
    #
    # Ordered by: standard name
    #
    # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    #      1    0.009    0.009    1.392    1.392 <string>:1(<module>)
    #      1    1.180    1.180    1.383    1.383 task_2.py:31(sieve)
    #      5    0.071    0.014    0.071    0.014 task_2.py:43(<listcomp>)
    #      5    0.089    0.018    0.089    0.018 task_2.py:52(<listcomp>)
    #      1    0.042    0.042    0.042    0.042 task_2.py:56(<listcomp>)
    #      1    0.000    0.000    1.392    1.392 {built-in method builtins.exec}
    #      5    0.000    0.000    0.000    0.000 {built-in method builtins.len}
    #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

    c_run('prime(90000)')
    #           90006 function calls in 5.641 seconds
    #
    # Ordered by: standard name
    #
    # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    #      1    0.000    0.000    5.641    5.641 <string>:1(<module>)
    #      1    0.000    0.000    5.641    5.641 task_2.py:60(prime)
    #  90001    5.631    0.000    5.631    0.000 task_2.py:61(_primes)
    #      1    0.000    0.000    5.641    5.641 {built-in method builtins.exec}
    #      1    0.010    0.010    5.641    5.641 {built-in method builtins.next}
    #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Заключение:
# Первый алгоритм («Решето Эратосфена») работает быстрее, после N = 6000
# До этого выигрывает второй алгоритм, но не намного.
# Можно сделать вывод, что первый алгоритм работает лучше
