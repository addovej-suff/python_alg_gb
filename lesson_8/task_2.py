# Закодируйте любую строку по алгоритму Хаффмана.

from collections import Counter
from heapq import heapify, heappop, heappush


class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def walk(self, cd, acc):
        self.left.walk(cd, acc + '0')
        self.right.walk(cd, acc + '1')


class Leaf:
    def __init__(self, letter):
        self.letter = letter

    def walk(self, cd, acc):
        cd[self.letter] = acc or '0'


class Huffman:
    def __init__(self, s):
        self.s = s
        self.map = self._create_map()

    def _create_map(self):
        h = []
        for ch, freq in Counter(self.s).items():
            h.append((freq, len(h), Leaf(ch)))
        heapify(h)
        count = len(h)
        while len(h) > 1:
            freq_1, _, left = heappop(h)
            freq_2, _, right = heappop(h)
            heappush(h, (freq_1 + freq_2, count, Node(left, right)))

            count += 1

        code = {}
        if h:
            [(_freq, _, root)] = h
            root.walk(code, '')
        return code

    def encode(self):
        return ''.join(self.map[ch] for ch in string)

    def decode(self, encoded):
        decoded = ''
        enc_ch = ''
        for ch in encoded:
            enc_ch += ch
            for dec_ch in self.map:
                if self.map.get(dec_ch) == enc_ch:
                    decoded += dec_ch
                    enc_ch = ''
                    break
        return decoded

    def test(self):
        assert self.decode(self.encode()) == self.s, 'Check your alg'
        print('Test passed')


string = input('Введите строку: ')
huffman = Huffman(string)
encoded_str = huffman.encode()

print('Карта:')
print('\n'.join(f'{ch}: {huffman.map[ch]}' for ch in sorted(huffman.map)))

print(f'Закодированная строка: {encoded_str}')
print(f'Декодированная строка: {huffman.decode(encoded_str)}')
