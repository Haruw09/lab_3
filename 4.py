import turtle

turtle.speed(20)


def f(x, y, Vx, Vy):
    ay = -10
    dt = 0.01
    s = Vy
    t = 0
    while t <= 2 * s / 10:
        x += Vx * dt
        y += Vy * dt + ay * dt ** 2 / 2
        Vy += ay * dt
        t += dt

        turtle.goto(x, y)


x0 = 0
y0 = 0
Vx0 = 20
Vy0 = 30
const = 0.7

for j in range(int(input())):
    f(x0, 0, Vx0, Vy0)
    x0 += Vx0 * 2 * Vy0 / 10
    Vx0 *= const
    Vy0 *= const
