# Урок 3. Массивы. Кортежи. Множества. Списки.
from random import randrange
from beautifultable import BeautifulTable
def create_array(a, b, x, y):
    m1 = []
    for i in range(int(randrange(a, b))):
        m1.append(randrange(x, y))
    return m1

def create_bf_matrix(a, b, x, y):
    beautiful_matrix = BeautifulTable()
    row = 0
    matr = []
    for i in range(b):
        matr.append([])
        row += 1
        for j in range(a):
            matr[i].append(randrange(x, y))
    for i in matr:
        beautiful_matrix.append_row(i)
    return beautiful_matrix

# 1. В диапазоне натуральных чисел от 2 до 1000000 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

count_l = 0
for i in range(2, 1000001):
    for j in range(2, 10):
        if i % j == 0:
            #print(i, j)
            count_l += 1
print(count_l)

# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями  8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

m1 = create_array(10, 20, 1, 50)
m2 = []
for i in range(len(m1)):
    if m1[i] % 2 == 0:
        m2.append(i)
print(m1)
print('Индексы четных элементов: ', m2)

# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

m1 = create_array(10, 20, 1, 50)
print(m1)
indmax, indmin = m1.index(max(m1)), m1.index(min(m1))
m1[indmax], m1[indmin] = m1[indmin], m1[indmax]
print(m1)
print(max(m1), min(m1))

# 4. Определить, какое число в массиве встречается чаще всего.

m1 = create_array(30, 50, 1, 18)
print(m1)
num = m1[0]
max_freq = 1
for i in range(len(m1)):
    freq = 1
    for j in range(i + 1, len(m1)):
        if m1[i] == m1[j]:
            freq += 1
    if freq > max_freq:
        max_freq = freq
        num = m1[i]
if max_freq > 1:
    print('Число', num, 'встречается', max_freq, 'раз(а)', )
else:
    print('Все элементы массива уникальны')

# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

m1 = create_array(10, 20, -50, 50)
print(m1)
num = min(m1)
for i in range(len(m1)):
    if num < m1[i] < 0:
        num = m1[i]
print('Максимальное число из отрицательных %d, находится на %d-ой позиции' % (num, m1.index(num)))

# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

m1 = create_array(10, 20, 0, 50)
print(m1)
min_element, max_element = m1.index(min(m1)), m1.index(max(m1))
sum_element = 0
print(m1.index(min(m1)), m1.index(max(m1)))
if m1.index(min(m1)) > m1.index(max(m1)):
    min_element, max_element = m1.index(max(m1)), m1.index(min(m1))
for i in range(min_element + 1, max_element ):
    sum_element = sum_element + m1[i]
    # print(m1[i])
print('Сумма элементов, находящихся между минимальным и максимальным элементами равна %d' % (sum_element))

# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться
# минимальными), так и различаться.

m1 = create_array(10, 20, 0, 20)
m2 = []
print(m1)
min_element = min(m1)
# print(min_element, m1.count(min_element))
if m1.count(min_element) > 1:
    print('Оба наименьших элемента равны %d' % (min_element))
else:
    for i in range(len(m1)):
        if m1[i] != min(m1):
            m2.append(m1[i])
            second_min = min(m2)
    print('Минимальное №1 %d' % (min_element))
    print('Минимальное №2 %d' % (second_min))

# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму введенных
# элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.

from beautifultable import BeautifulTable

bt = BeautifulTable()
row = 0
matr = []
print('Составьте матрицу 4х4')
for i in range(4):
    matr.append([])
    row += 1
    print('Введите числа %d-й строки: ' % row)
    for j in range(4):
        matr[i].append(int(input(':')))
for i in matr:
    i.append(sum(i))
    bt.append_row(i)
print(bt)

# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

rows_in_matrix, lines_in_matrix = 8, 5
bf_matrix = create_bf_matrix(rows_in_matrix, lines_in_matrix, 0, 50)
print(bf_matrix)
m2 = []
for j in range(rows_in_matrix):
    m1 = []
    for i in range(lines_in_matrix):
        m1.append(bf_matrix[i][j])
    m2.append(min(m1))

print('Минимальные по столбцам: ', m2)
print("Максимальный среди минимальных элементов столбцов: ", max(m2))

