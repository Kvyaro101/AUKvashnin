"""Модуль, рисующий с помощью черепашьей графики то, что я смог придумать: дерево и куст"""
import turtle as tl
import random

wn = tl.Screen()
wn.bgcolor('ghostwhite')
def draw_circles(size,space,number,color):
    """Функция описывает круги уменьшающегося радиуса"""
    for i in range(number):
        tl.color(color)
        tl.circle(size)
        size=size-space
def draw_special(size,repeat,space,number,color):
    """Фукнция, отвечающая за поворот кругов. Size – размер, repeat – повторения по кругу;
    space – шаг радиуса; num – число "однонаправленных" кругов; col – цвет, sp – скорость"""
    for i in range (repeat):
        draw_circles(size,space,number,color)
        tl.right(360/repeat)

colors = ("firebrick", "magenta", "steelblue", "coral", "navy", "cyan", "palevioletred")
"""Для разного, просто список забавных цветов"""

def draw_fractal(size):
    """Функция, описывающая геометрию дерева"""
    if size >= 5:
        if size >120: #Чтобы ствол и ветки были разных цветов
            tl.color("saddlebrown")
        else:
            tl.color("green")
        tl.pensize(max(size / 50, 1))
        tl.forward(size)
        tl.left(40)
        draw_fractal(size / 2) #Разные коэффициенты для асимметрии дерева
        tl.right(20)
        draw_fractal(size / 1.5)
        tl.right(40)
        draw_fractal(size / 1.7)
        tl.left(20)
        tl.penup()
        tl.backward(size)
        tl.pendown()
    else:
        tl.color(random.choice(colors))
        tl.circle(2)

def little_brush(size):
    """Функция, описывающая геометрию 1 ветки куста"""
    if size >= 5:
        tl.color("green")
        tl.pensize(max(size / 50, 1))
        tl.forward(size)
        tl.left(40)
        draw_fractal(size*0.7) #Слои куста:средний 0.7, внутренний 0.6 и внешний 5/3
        tl.right(60)
        draw_fractal(size*0.4)
        tl.right(20)
        draw_fractal(size/0.6)
        tl.left(40)
        tl.penup()
        tl.backward(size)
        tl.pendown()
    else:
        tl.color(random.choice(colors))
        tl.dot(4)

def brush_formation(size):
    """Функция, формирующая направления основных веток куста"""
    little_brush(size*1.3)
    tl.left(30)
    little_brush(size*1.2)
    tl.left(45)
    little_brush(size*1)
    tl.left(40)
    little_brush(size*1.2)
    tl.left(35)
    little_brush(size*1.3)

tl.tracer(False) # Отключение анимации рисовки

screen = tl.Screen() #Просто переобозначение

tl.penup() # Начальные условия для дерева
tl.goto(-screen.window_width()*0.45, -screen.window_height()*0.7) # Для универсальности
tl.setheading(90)
tl.pendown()

draw_fractal(300)

tl.penup()
tl.goto(screen.window_width()*0.6, screen.window_height()*0.45) # Для универсальности
tl.setheading(45)
tl.pendown()

draw_special(40,8,2,10,"orangered")
draw_special(60,10,3,8,"gold")

tl.penup() # Начальные условия для куста
tl.color('green')
tl.goto(screen.window_width()*0.45, -screen.window_height()*0.5)
tl.setheading(30)
tl.pendown()

brush_formation(40)

tl.done()
