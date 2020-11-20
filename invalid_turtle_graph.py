"""Модуль, рисующий с помощью черепашьей графики то, что я смог придумать: абстракцию и дерево"""
import turtle as tl
import random
wn = tl.Screen()
wn.bgcolor('black')
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
"""Для шариков, просто список забавных цветов"""

def tree (size,plush):
    """Основная функция. Использует все последующие для краткости"""
    tl.color('green')
    tl.pensize(max(size / 100, 1))
    tl.forward(size)
    tl.left(130)
    branch(size,plush,1) #Постройка 1 пары веток
    tl.left(100)
    branch(size,plush,0)
    shift(size)
    branch(size*1.2,plush*2,1) #Постройка 2 пары веток
    tl.left(100)
    branch(size*1.2,plush*2,0)
    shift(size)
    branch(size*1.6,plush*3,1) #Постройка 3 пары веток
    tl.left(100)
    branch(size*1.6,plush*3,0)
    shift(size)
    branch(size*1.8,plush*4,1) #Постройка 4 пары веток
    tl.left(100)
    branch(size*1.8,plush*4,0)
    tl.pensize(max(size/100,1))
    tl.right(50)
    tl.color ("saddlebrown") #Подкрашивание нижней части в цвет похожий на кору
    tl.forward(size*2/5) #Т.к. ветки сдвигали на 1/5 длины, а их было 4, то осталось 2/5 ствола
    tl.penup()
    tl.backward(size)
    tl.right(30) #Рисование звезды
    tl.forward(8)
    tl.left(180)
    tl.pendown()
    tl.begin_fill()
    tl.color("red")
    for i in range(5):
        tl.forward(25)
        tl.left(144)
    tl.end_fill()
    tl.hideturtle()

def sphere ():
    """Функция описывает рисование шарика ниже ветки"""
    tl.begin_fill()
    tl.color(random.choice(colors))
    tl.circle(6)
    tl.color(random.choice(colors))
    tl.end_fill()
    tl.color("green")


def branch (size, plush, brandh_side):
    """Фунция описывает рисование самой ветки, иголок, шариков на ней"""
    tl.pensize(max(size / 200, 1))
    tl.forward(size/4)
    sphere()
    for i in range (plush): #Plush – параметр, который пропорционален числу иголок
        tl.pensize(1) #По сути, здесь прописано, чтобы рисовались иголки и только они
        tl.right(25)
        tl.forward(18)
        tl.penup()
        tl.backward(18)
        tl.pendown()
        tl.left(50)
        tl.forward(18)
        tl.penup()
        tl.backward(18)
        tl.pendown()
        tl.right(25)
        tl.backward(size/(4*plush))
        if i % 7 == 0: #Условие, чтобы пририсовывались шарики при каждом 7 паре иголок
            tl.penup()
            if (brandh_side % 2) == 1: #Условие, чтобы шарики висели снизу от ветки
                tl.left(70)
                tl.forward(4)
                tl.pendown()
                sphere()
                tl.penup()
                tl.backward(4)
                tl.right(70)
            else:
                tl.right(70)
                tl.forward(8)
                tl.pendown()
                sphere()
                tl.penup()
                tl.backward(8)
                tl.left(70)
            tl.pendown()
        else:
            pass
def shift (size):
    """Функция отвечает за смещение после прорисовывания пары веток, иголки на стволе"""
    tl.penup()
    tl.right(50)
    tl.down()
    for i in range (20): #Описание формирования иголок на стволе. Аналогично веткам
        tl.pensize(1)
        tl.right(25)
        tl.forward(18)
        tl.penup()
        tl.backward(18)
        tl.pendown()
        tl.left(50)
        tl.forward(18)
        tl.penup()
        tl.backward(18)
        tl.pendown()
        tl.right(25)
        tl.forward(size/(5*20))
    tl.right(50)

tl.speed(0)

draw_special(100,6,6,10,"maroon")
draw_special(200,19,4,4,"violet")
draw_special(130,15,7,4,"pink")
draw_special(120,14,2,4,"orange")
draw_special(180,19,6,4,"lightblue") #Вызываем круги разных радиусов, шагов, цветов

tl.clear() # Чтобы не было нагромождения

tl.penup() #Начальные условия для рисования дерева
tl.goto(0,-400)
tl.setheading(90)
tl.pendown()

tree(600,10)

tl.done() #Чтобы Питон не закрывал результат
