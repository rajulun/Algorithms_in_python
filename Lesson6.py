# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# № 1
import memory_profiler
from random import randrange

@memory_profiler.profile

def create_array(a, b, x, y):
    m1 = []
    for i in range(int(randrange(a, b))):
        m1.append(randrange(x, y))
    return m1
def a():
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
# ===============================================================
# =============++++ Python 3.7 Win 10 64 бит ++++================
# Line #    Mem usage    Increment   Line Contents
# ================================================
#      7     14.5 MiB     14.5 MiB   @memory_profiler.profile
#      8
#      9                             def create_array(a, b, x, y):
#     10     14.5 MiB      0.0 MiB       m1 = []
#     11     14.5 MiB      0.0 MiB       for i in range(int(randrange(a, b))):
#     12     14.5 MiB      0.0 MiB           m1.append(randrange(x, y))
#     13     14.5 MiB      0.0 MiB       return m1
#
#
# [11, 1, 19, 13, 3, 17, 14, 16, 17, 19]
# Минимальное №1 1
# Минимальное №2 3
# ===============================================================

# №2
from beautifultable import BeautifulTable
import memory_profiler

@memory_profiler.profile

def b():
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

b()

# ===============================================================
# =============++++ Python 3.7 Win 10 64 бит ++++================
# Line #    Mem usage    Increment   Line Contents
# ================================================
    #  4     14.0 MiB     14.0 MiB   @memory_profiler.profile
    #  5
    #  6                             def b():
    #  7     14.0 MiB      0.0 MiB       bt = BeautifulTable()
    #  8     14.0 MiB      0.0 MiB       row = 0
    #  9     14.0 MiB      0.0 MiB       matr = []
    # 10     14.0 MiB      0.0 MiB       print('Составьте матрицу 4х4')
    # 11     14.0 MiB      0.0 MiB       for i in range(4):
    # 12     14.0 MiB      0.0 MiB           matr.append([])
    # 13     14.0 MiB      0.0 MiB           row += 1
    # 14     14.0 MiB      0.0 MiB           print('Введите числа %d-й строки: ' % row)
    # 15     14.0 MiB      0.0 MiB           for j in range(4):
    # 16     14.0 MiB      0.0 MiB               matr[i].append(int(input(':')))
    # 17     14.0 MiB      0.0 MiB       for i in matr:
    # 18     14.0 MiB      0.0 MiB           i.append(sum(i))
    # 19     14.0 MiB      0.0 MiB           bt.append_row(i)
    # 20     14.0 MiB      0.0 MiB       print(bt)
# ===============================================================


# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность вашей ОС.