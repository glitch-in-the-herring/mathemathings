from math import dist

def clength(x, y, a, b, n):
    dt = (b - a) / n
    t = a
    l = 0
    x_0, y_0 = x(a), y(a)

    for i in range(n):
        x_t, y_t = x(t + dt), y(t + dt)
        l += dist((x_0, y_0), (x_t, y_t))
        x_0, y_0 = x_t, y_t
        t += dt

    return l
