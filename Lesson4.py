# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

from random import randrange
import timeit
import cProfile as cp
import math, sys

# Урок 3, задание 1. В диапазоне натуральных чисел от 2 до 1000000 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
def create_array(a, b, x, y):
    m1 = []
    for i in range(int(randrange(a, b))):
        m1.append(randrange(x, y))
    return m1
n = 10
def calculate(n):
    k = 0
    while k <= n:
        count_l = 0
        for i in range(2, 1000001):
            for j in range(2, 10):
                if i % j == 0:
                    count_l += 1
        k += 1
    print('======>>> ', count_l)
    print(f'Прогоняем Урок 3, задание 1.  {n} раз')
    return count_l

def calculate1(n):
    k = 0
    while k <= n:
        b = 2
        count_l = 0
        while b <= 1000000:
            c = 2
            while c <= 9:
                if b % c == 0:
                    count_l += 1
                c += 1
            b += 1
        k += 1
    print('======>>> ', count_l)
    print(f'Прогоняем немного измененный Урок 3, задание 1.  {n} раз')
    return count_l

cp.run('calculate(n)')

cp.run('calculate1(n)')

# ======>>>  1828967
# Прогоняем Урок 3, задание 1.  10 раз
#          6 function calls in 30.986 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000   30.986   30.986 <string>:1(<module>)
#         1   30.985   30.985   30.986   30.986 scratch_4.py:13(calculate)
#         1    0.000    0.000   30.986   30.986 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}




# ======>>>  1828967
# Прогоняем немного измененный Урок 3, задание 1.  10 раз
#          6 function calls in 41.503 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000   41.503   41.503 <string>:1(<module>)
#         1   41.503   41.503   41.503   41.503 scratch_4.py:26(calculate1)
#         1    0.000    0.000   41.503   41.503 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов. Результаты анализа сохранить в виде комментариев в файле с кодом.

### 2. Написать два алгоритма нахождения i-го по счёту простого числа.

n = int(input('Введите порядковый номер простого числа: '))

### Без использования «Решета Эратосфена»;

def bez_resheta(n):
    primes = []
    for i in range(2, 10000):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    print(f'Искомое простое число = {primes[n - 1]} (без Решета Эратосфена)')

cp.run('bez_resheta(n)')

print('======================================')

### Используя алгоритм «Решето Эратосфена»

def resheto(n):
    primes = []
    nums = [i for i in range(2, 10000)]
    for i in nums:
        if i != 0:
            primes.append(i)
            for j in nums[i:]:
                if j % i == 0:
                    nums[j - 2] = 0
    print(f'Искомое простое число = {primes[n - 1]} (с алгоритмом «Решето Эратосфена»)')

cp.run('resheto(n)')

# Введите порядковый номер простого числа: 1111
# Искомое простое число = 8933 (без Решета Эратосфена)
#          1234 function calls in 1.399 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    1.399    1.399 <string>:1(<module>)
#         1    1.398    1.398    1.399    1.399 scratch_1.py:9(bez_resheta)
#         1    0.000    0.000    1.399    1.399 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#      1229    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# ======================================
# Искомое простое число = 8933 (с алгоритмом «Решето Эратосфена»)
#          1235 function calls in 2.187 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    2.187    2.187 <string>:1(<module>)
#         1    2.184    2.184    2.187    2.187 scratch_1.py:42(resheto)
#         1    0.002    0.002    0.002    0.002 scratch_1.py:44(<listcomp>)
#         1    0.000    0.000    2.187    2.187 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#      1229    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}