# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами
# на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована
# в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
import random

massiv_for_sort = [random.randint(-100, 100) for i in range(15)]
print(f'Сгенерированный список :\n{massiv_for_sort}')


def bubble_sort(massiv_for_sort):
    n = 1
    while n < len(massiv_for_sort):
        sorted = True
        for i in range(len(massiv_for_sort) - n):
            if massiv_for_sort[i] < massiv_for_sort[i + 1]:
                massiv_for_sort[i], massiv_for_sort[i + 1] = massiv_for_sort[i + 1], massiv_for_sort[i]
                sorted = False

        if sorted == True:
            break
        n += 1
    print(f'Отсортированный по убыванию список:\n{massiv_for_sort}')


bubble_sort(massiv_for_sort)

# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

def merge_sort(a):
    n = len(a)
    if n < 2:
        return a

    l = merge_sort(a[:n//2])
    r = merge_sort(a[n//2:n])

    i = j = 0
    res = []
    while i < len(l) or j < len(r):
        if not i < len(l):
            res.append(r[j])
            j += 1
        elif not j < len(r):
            res.append(l[i])
            i += 1
        elif l[i] < r[j]:
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            j += 1
    return res

A = [round(random.uniform(0, 50, ), 2) for i in range(15)]
print(f'Сгенерированный список :\n{A}')
A = merge_sort(A)
print(f'Отсортированный по возрастанию список:\n{A}')
# print( *A )

# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
# в другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# то используйте метод сортировки, который не рассматривался на уроках

m = 4
len_massiv = 2 * m + 1
massiv = [random.randint(1, 50) for i in range(len_massiv)]

print(f'Сгенерированный список:\n{massiv}')


def median(massiv):

    for i in massiv:
        num = i
        b = 0
        for j in massiv:

            if i < j:
                b += 1

        if len(massiv) == 2 * b + 1:
            return num


print(f'\nМедиана cгенерированного списка: {median(massiv)}\n')
print(f'Отсортированный по возрастанию список:\n{sorted(massiv)}')

