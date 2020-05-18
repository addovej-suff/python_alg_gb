# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

# Блок-схема: https://drive.google.com/open?id=1C0AIc35EQ2UT1sybTyS-qwI3AKeJJwy2


def digit_count(_numbers_count, _digit, _count=0, _counter=1):
    number = input('Введите число: ')

    for dig in number:
        if dig == _digit:
            _count += 1

    if _counter == _numbers_count:
        return _count
    return digit_count(_numbers_count, _digit, _count, _counter + 1)


numbers_count = int(input('Введите количество чисел: '))
digit = input('Введите цифру, которую хотите считать: ')

count = digit_count(numbers_count, digit)

print(f'Цифра {digit} встречается {count} раз')
