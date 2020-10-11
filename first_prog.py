#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import numpy
import matplotlib.pyplot as mpp # Импорт пакетов math, numpy и matplotlib.pyplot

# Эта программа рисует график функции, заданной выражением ниже

if __name__=='__main__':
    arguments = numpy.r_[0:200:0.1] # Задание значения аргументов: от 0 до 200 с шагом в 0.1
    mpp.plot(
        arguments,
        [math.sin(a) * math.sin(a/20.0) for a in arguments]
    ) # Описание графика: взяты функции sin из библиотеки math, выполнены для обозначенных выше аргументов 
    mpp.show() # Вывод графика