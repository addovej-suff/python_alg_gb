# Пользователь вводит номер буквы в алфавите. Определить, какая это буква

# Блок-схема: https://drive.google.com/open?id=1Mb3nxW5B_Xbh2wN7RyawK_5kkR8pPdB6

letter_number = int(
    input('Введите целое число номера буквы в латинском алфавите (1-26): ')
)

shift = ord('a') - 1

letter = chr(letter_number + shift)

print(f'Буква: {letter}')
