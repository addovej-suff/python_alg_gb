# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

# Блок-схема: https://drive.google.com/open?id=1Mb3nxW5B_Xbh2wN7RyawK_5kkR8pPdB6

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

if a < b < c or c < b < a:
    res = b
elif b < a < c or c < a < b:
    res = a
else:
    res = c

print(f'Среднее число: {res}')
