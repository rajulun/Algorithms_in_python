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


