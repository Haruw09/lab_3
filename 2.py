import turtle

turtle.shape('turtle')
l = 10
d = 200 ** 0.5
a1 = 90
a2 = 45

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

d0 = [(0, l), (-a1, 2 * l), (-a1, l), (-a1, 2 * l), (-a1, l)]
d1 = [(a1 + a2, d), (-a1 - a2, 2 * l), (2 * a1, 2 * l), (-a1, 0)]
d2 = [(0, l), (-a1, l), (-a2, d), (a1 + a2, l)]
d3 = [(0, l), (-a1 - a2, d), (a1 + a2, l), (-a1 - a2, d)]
d4 = [(-a1, l), (a1, l), (-a1, l), (2 * a1, 2 * l), (-a1, 0)]
d5 = [(0, l), (2 * a1, l), (a1, l), (a1, l), (-a1, l), (-a1, l)]
d6 = [(0, l), (a1, l), (a1, l), (a1, l), (-a1 - a2, d), (-a2, 0)]
d7 = [(0, l), (-a1 - a2, d), (a2, l)]
d8 = [(-a1, l), (a1, l), (-a1, l), (-a1, l), (-a1, 2 * l), (-a1, l), (-a1, l), (a1 * 2, l), (-a1, 0)]
d9 = [(-a1, l), (a1, l), (-a1 - a2, d), (a1 * 2, d), (a2, l), (a1, l), (a1 * 2, l)]

dfont = [d0, d1, d2, d3, d4, d5, d6, d7, d8, d9]

for i in range(6):
    f(int(input()))
    whitespace()