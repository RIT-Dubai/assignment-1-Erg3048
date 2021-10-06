import turtle as t


XMAX = 200
XMIN = -XMAX
YMAX = 200
YMIN = -YMAX


def grid():
    t.penup()
    t.goto(XMIN, YMAX)
    t.pendown()
    for i in range(4):
        t.forward(400)
        t.right(90)


