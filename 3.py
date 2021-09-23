import turtle

turtle.shape('turtle')
inp = open('index_numbers.txt', 'r')

def f(x):
    if x == 1:
        turtle.penup()
        turtle.left(3 * a1)
        turtle.forward(l)
        turtle.pendown()
    if x == 6:
        turtle.penup()
        turtle.left(-a1)
        turtle.forward(l)
        turtle.pendown()
    for angle, length in dfont[x]:
        turtle.left(angle)
        turtle.forward(length)
    if x == 2:
        turtle.penup()
        turtle.left(a1)
        turtle.forward(2 * l)
        turtle.left(-a1)
    if x == 3:
        turtle.penup()
        turtle.left(a1 + a2)
        turtle.forward(l)
        turtle.left(a1)
        turtle.forward(2 * l)
        turtle.left(-a1)
    if x == 5:
        turtle.penup()
        turtle.left(2 * a1)
        turtle.forward(l)
        turtle.left(a1)
        turtle.forward(2 * l)
        turtle.left(-a1)
    if x == 7:
        turtle.penup()
        turtle.left(a1)
        turtle.forward(l)
        turtle.left(a1)
        turtle.forward(2 * l)
        turtle.right(a1)

def whitespace():
    turtle.penup()
    turtle.forward(l)
    turtle.pendown()

d0 = inp.readline()
d1 = inp.readline()
d2 = inp.readline()
d3 = inp.readline()
d4 = inp.readline()
d5 = inp.readline()
d6 = inp.readline()
d7 = inp.readline()
d8 = inp.readline()
d9 = inp.readline()

dfont = [d0, d1, d2, d3, d4, d5, d6, d7, d8, d9]

for i in range(6):
    f(int(input()))
    whitespace()

inp.close()