# По введенным пользователем координатам двух точек вывести уравнение прямой вида
# y = kx + b, проходящей через эти точки

# Блок-схема: https://drive.google.com/open?id=1Mb3nxW5B_Xbh2wN7RyawK_5kkR8pPdB6

x1 = float(input('Введите x1: '))
y1 = float(input('Введите y1: '))
x2 = float(input('Введите x2: '))
y2 = float(input('Введите y1: '))

if x1 == x2:
    res = f'x = {x1}'
elif y1 == y2:
    res = f'y = {y1}'
else:
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k*x2
    res = f'y = {k}x + {b}'

print(res)
