# Написать программу сложения и умножения
# двух шестнадцатеричных чисел. При этом каждое число
# представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как
# [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из
# примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque
from random import randint

HEX_BASE = 16


def test(func):
    print(f'Test function \x1b[1;37;33m{func.__name__}\x1b[0m')
    _size = 30
    _min = 1
    _max = 1000
    numbers_set = [
        (hex(randint(_min, _max))[2:], hex(randint(_min, _max))[2:]) for _ in range(_size)
    ]
    print(f'Tests count: {len(numbers_set)}')

    for num_1, num_2 in numbers_set:
        res = hex(int(num_1, HEX_BASE) + int(num_2, HEX_BASE))[2:] \
            if func.__name__ == 'addition' else \
            hex(int(num_1, HEX_BASE) * int(num_2, HEX_BASE))[2:]
        res_test = ''.join(func(deque(num_1), deque(num_2)))

        assert res == res_test, f'{res} != {res_test}'
        print('OK', end=' ')
    print()


def addition(number_1: deque, number_2: deque) -> deque:
    len_number_1 = len(number_1)
    len_number_2 = len(number_2)

    # Need add insignificant zeros to the begin for length equals
    if len_number_1 != len_number_2:
        if len_number_1 < len_number_2:
            number_1.extendleft('0' * (len_number_2 - len_number_1))
        else:
            number_2.extendleft('0' * (len_number_1 - len_number_2))

    number_1.reverse()
    number_2.reverse()

    result = deque()
    _mem = None
    for i in range(len(number_1)):
        _tmp = int(number_1[i], HEX_BASE) + int(number_2[i], HEX_BASE)
        if _mem is not None:
            _tmp += int(_mem, HEX_BASE)
            _mem = None

        _res = hex(_tmp)[2:]  # lstrip returns '' when 0x0
        if len(_res) > 1:
            if i == len(number_1) - 1:  # Check last iteration
                result.extendleft(_res[::-1])  # Add all reversed sequence
            else:
                _mem = _res[:-1]  # Memorize all except last
                result.appendleft(_res[-1])  # Add latest
        else:
            result.appendleft(_res)
    return result


def multiplication(number_1: deque, number_2: deque) -> deque:
    number_1.reverse()
    number_2.reverse()

    tmp_results = []
    for i, digit_1 in enumerate(number_1):
        _mem = None
        tmp_res = deque('0' * i)  # Shift pos for following sum
        for j, digit_2 in enumerate(number_2):
            _tmp = int(digit_1, HEX_BASE) * int(digit_2, HEX_BASE)
            if _mem is not None:
                _tmp += int(_mem, HEX_BASE)
                _mem = None

            _res = hex(_tmp)[2:]  # lstrip returns '' when 0x0
            if len(_res) > 1:
                if j == len(number_2) - 1:  # Check last iteration
                    tmp_res.extendleft(_res[::-1])  # Add all reversed sequence
                else:
                    _mem = _res[:-1]  # Memorize all except last
                    tmp_res.appendleft(_res[-1])  # Add latest
            else:
                tmp_res.appendleft(_res)
        tmp_results.append(tmp_res)

    if len(tmp_results) == 1:
        return tmp_results[0]
    else:
        result = None
        for i in range(1, len(tmp_results)):
            if result is None:
                result = addition(tmp_results[i - 1], tmp_results[i])
            else:
                result = addition(result, tmp_results[i])

    return result


# Tests
test(addition)
test(multiplication)

first = deque(input('Введите первое число в HEX: '))
second = deque(input('Введите второе число в HEX: '))

print(f'Сумма: {list(addition(first.copy(), second.copy()))}')
print(f'Произведение: {list(multiplication(first.copy(), second.copy()))}')
