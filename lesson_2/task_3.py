# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32
# и заканчивая 127-м включительно. Вывод выполнить в табличной форме:
# по десять пар "код-символ" в каждой строке.

# Блок-схема: https://drive.google.com/open?id=1C0AIc35EQ2UT1sybTyS-qwI3AKeJJwy2


BEGIN = 32
END = 128
res = ''

for i in range(BEGIN, END):
    k = i - BEGIN
    val = f'{i}-{chr(i)}'
    if k % 10 == 0:
        res += f'\n{val:10}'
    else:
        res += f'{val:10}'

print(res)
