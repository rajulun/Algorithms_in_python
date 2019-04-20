# 1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
# состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.

input_string = input("Введите строку для подсчета подстрок: ")

print("Строка \'%s\' имеет длину %d сиволов." % (input_string, len(input_string)))

substrings = set()

for i in range(len(input_string)):

    for j in range(len(input_string) - 1 if i == 0 else len(input_string), i, -1):
        substrings.add(hash(input_string[i:j]))

print("Количество различных подстрок в этой строке:", len(substrings))


# 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.

import heapq
from collections import Counter
from collections import namedtuple


class Node(namedtuple("Node", ["left", "right"])):  # класс для ветвей дерева - внутренних узлов; у них есть потомки
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):  # класс для листьев дерева, у него нет потомков, но есть значение символа
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def huffman_encode(s):
    h = []

    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)
    count = len(h)

    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = {}

    if h:
        [(_freq, _count, root)] = h
        root.walk(code, "")

    return code


def main():
    s = input('Введите строку для кодирования: ')
    code = huffman_encode(s)
    encoded = "".join(code[ch] for ch in s)
    # print(len(code), len(encoded))

    for ch in sorted(code):
        print("{}: {}".format(ch, code[ch]))
    print(encoded)


if __name__ == "__main__":
    main()
