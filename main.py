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


def rectangle_will_fit(x, y, l, h):
    if (x+l >= XMAX or x <= XMIN):
        return False
    if (y+h >= YMAX or y <= YMIN):
        return False

