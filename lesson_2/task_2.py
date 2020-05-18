# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

# Блок-схема: https://drive.google.com/open?id=1C0AIc35EQ2UT1sybTyS-qwI3AKeJJwy2

even_count = 0
odd_count = 0

number = input('Введите натуральное число: ')


for letter in number:
    digit = int(letter)
    if digit % 2 == 0:
        even_count += 1
    else:
        odd_count += 1


print(f'В {number} четных: {even_count}, нечетных: {odd_count}')
