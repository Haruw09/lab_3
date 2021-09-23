import turtle

def f(x, y, Vx, Vy):
    ay = -10
    dt = 0.01
    for i in range(1000):
        x += Vx * dt
        y += Vy * dt + ay * dt ** 2 / 2
        Vy += ay * dt

        turtle.goto(x, y)

Vx0 = 10
Vy0 = 15
const = 0.5
for j in range(int(input())):
    f(0, 0, Vx0, Vy0)
    Vx0 *= const
    Vy0 *= const