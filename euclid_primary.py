"""Все алгоритмы Евклида и простота"""

from math import sqrt
from timeit import timeit

def find_gcd(first_one, second_one):
    """Функция, считающая gcd и линейное представление его для двух чисел"""
    multiplier = 1
    num_1,num_2 = first_one,second_one
    while num_1 != 0 and num_2 != 0:
        if num_1>num_2:
            num_1 = num_1 % num_2
        else:
            num_2 = num_2 % num_1
    print ("gcd чисел",first_one, "и",second_one,":",max(num_1,num_2))
    num_1,num_2 = first_one/max(num_1,num_2), second_one/max(num_1,num_2) #Переисп. num_1 и num_2
    quotient = max(num_1,num_2)
    if num_1>num_2:
        while (num_1-1)%num_2!=0:
            num_1 += num_1 + quotient
            multiplier += 1
    else:
        while (num_2-1)%num_1!=0:
            num_2 += quotient
            multiplier += 1
    coefficient_1, coefficient_2 = multiplier, (multiplier*quotient-1)/min(num_1,num_2)

    print(f"Линейка:{coefficient_1}*{max(first_one,second_one)}+{coefficient_2}*{min(first_one,second_one)}={coefficient_1*max(first_one,second_one)-coefficient_2*min(first_one,second_one)}")

def primity(number):
    """Наивный способ подсчёта простоты"""
    divisor = []
    if number % 2!=0 or number==2:
        limit = int(sqrt(number)/2) - 1
        for i in range (limit+1):
            if divisor == [] and number % (3+2*i) == 0: #Хотя бы исключим чётные
                divisor.append(i)
        if limit==0 and number % 3 ==0:
            divisor.append(3)
    else:
        divisor.append(2)
    if divisor == []:
        return True

find_gcd(121,1555)
print(primity(2391))
print(primity(67280421310721))
print(f"Время 1 простоты:{timeit(lambda: primity(67280421310721), number=10) / 10}")
