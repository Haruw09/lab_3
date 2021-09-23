from random import *
import turtle

num = 30
steps_of_time_number = 100
dt = 0.1

v_x = [0 for i in range(num)]
v_y = [0 for i in range(num)]
turtle.penup()
turtle.goto(-200, -200)
turtle.pendown()
for i in range(4):
    turtle.forward(400)
    turtle.left(90)

pool = [turtle.Turtle(shape='circle') for i in range(num)]
for unit in pool:
    unit.turtlesize(0.3)
    unit.penup()
    unit.speed(50)
    unit.goto(randint(-200, 200), randint(-200, 200))
for i in range(num):
    v_x[i] = randint(-5, 5)
    v_y[i] = randint(-5, 5)
while True:
    for i in range(len(pool)):
        x = pool[i].xcor()
        y = pool[i].ycor()
        vx = v_x[i]
        vy = v_y[i]
        pool[i].goto(x + vx, y + vy)
        if x >= 193:
            v_x[i] = - abs(v_x[i])
        elif x <= -193:
            v_x[i] = abs(v_x[i])
        if y >= 193:
            v_y[i] = - abs(v_y[i])
        elif y <= -193:
            v_y[i] = abs(v_y[i])