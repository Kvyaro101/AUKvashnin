
import math
import cmath
import numpy as np
import matplotlib.pyplot as plt # Типичные библиотеки, as - просто замена обозначение и введение равносильного
cycle = 100 # Тут 1000, долго, но точно
def uti_puti_moi_logarifmic(x):
    """Вычисление логарифма при помощи частичного суммирования ряда Те́йлора"""
    x_pow = x # Значение части с x в степени
    multiplier = 1 # Множитель, т.е. остальная часть (без x в степени)
    partial_sum = x # Непосредственный результат неполной суммы
    for n in range(1, cycle):
        x_pow *= x  # Присвоение x_pow(er) значения = (пред)*на само себя 1 раз
        multiplier *= -1/(n + 1)*n  # Часть без икса, т.е. (-1)^n и (n+1)
        partial_sum += x_pow * multiplier # Присвоение partial_sum значения = (пред)+x_pow * multiplier
    
    return partial_sum # Питон, верни partial_sum, пожалуйста
vs = np.vectorize(uti_puti_moi_logarifmic) # А ещё преобразуй в вектора uti_puti_moi_logarifmic и запиши это в переменную vs
print(uti_puti_moi_logarifmic, vs) # Выдача результатов 
value = np.r_[-1:1:0.0001] # Данный метод работает только когда модуль значения меньше 1
plt.plot(value, np.log(value+1)) # Постройка графика, где по Х - value, а по Y - np.log(value+1)
plt.plot(value, vs(value)) # Постройка графика, где по Х - value, vs(value) 
plt.show() # Покажи, что получилось
"Часть с отрицательным логарифмом, все же знают самое красивое уравнение математики"
complex_value = -1
print('Значение аргумента, когда ему плохо и он отрицательны:', complex_value)
print("Достигает ли -1 наш логарифмик?", uti_puti_moi_logarifmic(complex_value)) # Нет, и не сможет никогда, ибо ограничение Те́йлора для логарифма: [-1,1]
print("А логарифм нормального человека?", cmath.log(complex_value)) # А вот этот смог