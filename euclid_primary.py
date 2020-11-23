"""Все алгоритмы Евклида и простота"""

from math import sqrt
from timeit import timeit

def find_gcd(first_one, second_one):
    """Функция, считающая gcd и линейное представление его для двух чисел"""
    multiplier = 1
    num_1,num_2 = first_one,second_one
    while num_1 != 0 and num_2 != 0: #gcd здесь. 1-ое число в результате
        if num_1>num_2:
            num_1 = num_1 % num_2
        else:
            num_2 = num_2 % num_1
    num_3,num_4 = first_one/max(num_1,num_2), second_one/max(num_1,num_2)
    quotient = max(num_3,num_4)
    if num_3>num_4:
        while (num_3-1)%num_4!=0:
            num_3 += num_3 + quotient
            multiplier += 1
    else:
        while (num_4-1)%num_3!=0:
            num_4 += quotient
            multiplier += 1
    coefficient_1, coefficient_2 = multiplier, -(multiplier*quotient-1)/min(num_3,num_4)
    return(max(num_1,num_2), [coefficient_1,coefficient_2,max(num_1,num_2)])

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
    return divisor == []

print(find_gcd(121,1111)) # Расширенный выдаёт 1-ым числом коэф. для max числа, 2-ым для min
print(primity(2391))
print(primity(67280421310721))
print(f"Время 1 простоты:{timeit(lambda: primity(67280421310721), number=10) / 10}")
