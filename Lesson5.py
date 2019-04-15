# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
# для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования
# предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
from collections import namedtuple

kol_vo = int(input('Введите количество предприятий :'))
enterprises = []
av_profit = 0
enterprise_profit = []
annual_profit = 0
all_profit = 0

for i in range(kol_vo):
    enterprises.append(input('Введите наименование предприятия:'))
    enterprise_profit = namedtuple('enterprise_profit', ['name','quarter1', 'quarter2', 'quarter3', 'quarter4', 'annual_profit'])
    quarter1, quarter2, quarter3, quarter4 = int(input('введите прибыль за 1 квартал: ')), \
    int(input('введите прибыль за 2 квартал: ')), int(input('введите прибыль за 3 квартал: ')), int(input('введите прибыль за 4 квартал: '))
    annual_profit = quarter1 + quarter2 + quarter3 + quarter4
    all_profit += annual_profit
    enterprises[i] = enterprise_profit(enterprises[i], quarter1, quarter2, quarter3, quarter4, annual_profit)
    print('Прибыль по %s - %d'% (enterprises[i][0], annual_profit))

av_profit = all_profit / kol_vo
print('Средняя прибыль по предприятиям = %d'% (av_profit))
high_profit = []
low_profit = []
for p in range(len(enterprises)):
    if enterprises[p][5] > av_profit:
        # print('Предприятия, у которых прибыль превышает среднегодовую по всем предприятиям')
        # print(enterprises[p][5], av_profit)
        high_profit.append(enterprises[p][0])
    elif enterprises[p][5] < av_profit:
        # print('Предприятия, у которых прибыль ниже среднегодового по всем предприятиям')
        # print(enterprises[p][5], av_profit)
        low_profit.append(enterprises[p][0])
print('Предприятия, у которых прибыль превышает среднегодовую по всем предприятиям', high_profit)
print('Предприятия, у которых прибыль ниже среднегодового по всем предприятиям', low_profit)


# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
# элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
# соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

def plus_hex(x, y):
    if len(x) > len(y):
        aaa, bbb = deque(reversed(x)), deque(reversed('0' * (len(x) - len(y)) + y))
    else:
        aaa, bbb = deque(reversed(y)), deque(reversed('0' * (len(y) - len(x)) + x))
    # print(aaa, bbb)
    cur_sum = '1'
    sss = deque()
    ss = ''
    for i in range(len(aaa)):
        if len(cur_sum) > 3:
            cur_sum = hex(int(aaa[i], 16) + int(bbb[i], 16) + int('1', 16))
        else:
            cur_sum = hex(int(aaa[i], 16) + int(bbb[i], 16))
        sss.appendleft(cur_sum[-1])
    for i in range(len(sss)):
        ss += sss[i]
    # print('ss', ss)
    return ss

def multiple_hex(x, y):
    fff = ''
    cur_mult = '0'
    perevod = '0'
    if len(x) > len(y):
        aaa, bbb = deque(reversed(x)), deque(reversed('0' * (len(x) - len(y)) + y))
    else:
        aaa, bbb = deque(reversed(y)), deque(reversed('0' * (len(y) - len(x)) + x))
    for i in range(len(bbb)):
        if len(cur_mult) > 3:
            mmm.appendleft(cur_mult[-2])
            fff += cur_mult[-2]
            if i > 1:
                fff = '0' * (i - 1) + fff
            cur_mult, perevod = '0', '0'
            mmm_for_plus.append(fff[::-1])
            fff = ''
        for p in range(len(aaa)):
            cur_mult = hex(int(aaa[p], 16) * int(bbb[i], 16) + int(perevod, 16))
            mmm.appendleft(cur_mult[-1])
            fff += cur_mult[-1]
            if len(cur_mult) > 3:
                perevod = cur_mult[-2]
            else:
                perevod = '0'
    return mmm_for_plus

# x = input('Введите первое шестнадцатеричное число: ')
# y = input('Введите второе шестнадцатеричное число: ')
x = 'A2f'
y = 'C4FF'
sss = plus_hex(x, y)
mmm = deque()
mmm_for_plus =deque()
print('Сумма чисел %s и %s равно %s'% (x, y, sss))

# print(hex(int(x, 16) * int(y, 16)))

deq_for_sum = multiple_hex(x, y)
sum_mult = ' '
# print(len(deq_for_sum))
for i in range(len(deq_for_sum) - 1):
    if i == 0:
        # print('1', deq_for_sum[i], deq_for_sum[i + 1])
        sum_mult = plus_hex(deq_for_sum[i], deq_for_sum[i + 1])
    else:
        # print('2', sum_mult, deq_for_sum[i + 1])
        sum_mult = plus_hex(sum_mult, deq_for_sum[i + 1])
print('Произведение чисел %s и %s равно %s'% (x, y, sum_mult))

# Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из модуля collections