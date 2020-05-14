# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

# Блок-схема: https://drive.google.com/open?id=1Mb3nxW5B_Xbh2wN7RyawK_5kkR8pPdB6


n = int(input('Введите трехзначное число (100-999): '))

first = n // 100
second = n % 100 // 10
third = n % 10

print(f'Сумма цифр числа: {first + second + third}')
print(f'Произведение цифр числа: {first * second * third}')
