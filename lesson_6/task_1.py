# Подсчитать, сколько было выделено памяти под переменные
# в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее
# эффективным использованием памяти.

# macOS Catalina
# Version: 10.15.4 (19E287) x64
# Python 3.7.3, CPython, 64bit

from collections import defaultdict
from random import randint
from sys import getsizeof, setprofile


F_S = '\x1b[1;37;33m'  # Start of string color format
F_E = '\x1b[0m'  # End of string color format


# Decorator for extraction local variables
class extract_locals:
    def __init__(self, func):
        self._locals = {}
        self.func = func
        self._name = func.__name__

    def __call__(self, *args, **kwargs):
        def inspector(frame, event, arg):
            if event == 'return':
                self._locals = frame.f_locals.copy()

        # Inspector is activated on next call, return or exception
        setprofile(inspector)
        try:
            # Inspect the function call
            res = self.func(*args, **kwargs)
        finally:
            # Disable inspector and replace with old
            setprofile(None)
        return res

    def clear_locals(self):
        self._locals = {}

    @property
    def locals(self):
        return self._locals

    @property
    def name(self):
        return self._name


class MemoryInfo(object):

    def __init__(self, functions: tuple):
        self.functions = functions
        self.res = []

    def __call__(self, with_details: bool = False, **kwargs):
        for func in self.functions:
            func_args = kwargs.get(func.name)
            if func_args:
                func(**func_args)
            else:
                func()
            func_mem = self.detailed_memory(func.locals)
            tmp = ''
            tmp += f'Функция {F_S}{func.name}{F_E} занимает ' \
                f'{F_S}{func_mem["all"]}{F_E} байт.'

            if with_details:
                tmp += '\n'
                for var, size in func_mem['variables_sizes'].items():
                    tmp += f'Переменная {var} заняла {size} байт\n'
            self.res.append(tmp)

    def calc_memory_size(self, obj: any) -> int:
        """
        Принимает любой объект и возвращает
        его суммарный размер занимаемой памяти
        :param obj: any
        :return: int
        """

        res = 0
        if not hasattr(obj, '__iter__') or isinstance(obj, str):
            res += getsizeof(obj)
        else:
            # Calculate full obj size
            res += getsizeof(obj)
            if hasattr(obj, 'items'):
                for key, value in obj.items():
                    # Calculate keys and values sizes
                    res += (self.calc_memory_size(key) + self.calc_memory_size(value))
            else:
                # Calculate iterable obj values sizes
                for item in obj:
                    res += self.calc_memory_size(item)

        return res

    def detailed_memory(self, objects: dict) -> dict:
        """
        Принимает в качестве параметра словарь с локальными переменными функции
        Возвращает детальную информацию по размеру для каждой переменной
        и суммарное количество занимаемой памяти по всем переменным.
        :param objects: dict
        :return: dict
        """

        # Prepare result
        res = {'variables_sizes': defaultdict(int), 'all': 0}

        # Iterate objects dict and store values sizes
        for var, val in objects.items():
            res['variables_sizes'][var] += self.calc_memory_size(val)

        # Calculate all sizes sum
        res['all'] = sum(res['variables_sizes'].values())

        return res


@extract_locals
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


@extract_locals
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


@extract_locals
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


memory_info = MemoryInfo((first, second, third))
memory_info(False, first={'size': 100}, second={'size': 100})
print(*memory_info.res, sep='\n')


# Для более детального анализа работы функций, было выбрано задание
# из 3-го ПЗ, которое было реализовано в 4-м ПЗ тремя способами и
# проанализировано для критерия времени выполнения.

# Результат выполнения тестирования
# Функция first занимает 1632 байт.
# Функция second занимает 1020 байт.
# Функция third занимает 1044 байт.

# Детальная информация:
# Функция first занимает 1632 байт.
# Переменная size заняла 28 байт
# Переменная max_item заняла 28 байт
# Переменная min_item заняла 28 байт
# Переменная array заняла 824 байт
# Переменная extremum заняла 584 байт
# Переменная i заняла 28 байт
# Переменная val заняла 28 байт
# Переменная start заняла 28 байт
# Переменная end заняла 28 байт
# Переменная _sum заняла 28 байт
#
# Функция second занимает 1020 байт.
# Переменная size заняла 28 байт
# Переменная max_item заняла 28 байт
# Переменная min_item заняла 28 байт
# Переменная array заняла 824 байт
# Переменная idx_min заняла 28 байт
# Переменная idx_max заняла 28 байт
# Переменная i заняла 28 байт
# Переменная _sum заняла 28 байт
#
# Функция third занимает 1044 байт.
# Переменная size заняла 28 байт
# Переменная max_item заняла 28 байт
# Переменная min_item заняла 28 байт
# Переменная array заняла 824 байт
# Переменная _max заняла 28 байт
# Переменная _min заняла 28 байт
# Переменная start заняла 24 байт
# Переменная end заняла 28 байт
# Переменная _sum заняла 28 байт


# Исходя из тестов памяти, эффективнее всех работает вторая функция
# Однако, опираясь на вывод первого задания 4-го урока, можно прийти к заключению,
# что оптимальнее всех по параметрам время выполнения/используемая память,
# будет третья функция, так как она является наиболее быстрой и по количеству используемой памяти
# отличается от второй всего на размер одной переменной (пример, 24 байта)
# PS: Из-за рандома количество
