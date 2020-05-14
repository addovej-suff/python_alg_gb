# Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

# Блок-схема: https://drive.google.com/open?id=1Mb3nxW5B_Xbh2wN7RyawK_5kkR8pPdB6

five = 5  # 101
six = 6  # 110

# Logic bit operation
bit_or = five | six  # 111
bit_and = five & six  # 100
bit_xor = five ^ six  # 011

bit_left = five << 2  # 10100
bit_right = five >> 2  # 1 (00001)


print(f'Результат побитового OR: {bit_or}')
print(f'Результат побитового AND: {bit_and}')
print(f'Результат побитового XOR: {bit_xor}')

print(f'Результат побитового сдвига {five} влево: {bit_left}')
print(f'Результат побитового сдвига {five} вправо: {bit_left}')

