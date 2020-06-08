# Определение количества различных подстрок с использованием
# хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.

from itertools import combinations

string = input('Введите строку: ')
hashes = set()

for i in range(1, len(string)):
    for item in combinations(string, i):
        _tmp = ''.join(item)
        if _tmp in string:
            hashes.add(hash(_tmp))

print(len(hashes))
