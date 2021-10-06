import turtle as t


XMAX = 200
XMIN = -XMAX
YMAX = 200
YMIN = -YMAX
PI = 3.1415926535


def grid():
    t.penup()
    t.goto(XMIN, YMAX)
    t.pendown()
    for i in range(4):
        t.forward(400)
        t.right(90)


def setup(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def rectangle_will_fit(x, y, l, h = 0):
    if (x+l >= XMAX or x <= XMIN):
        return False
    if (y+h >= YMAX or y <= YMIN):
        return False


def circle_will_fit(x, y, r):
    if (x+r >= XMAX or x-r <= XMIN):
        return False
    if (y+r >= YMAX or y-r <= YMIN):
        return False


def draw_shape(shape, color, x, y, l, h = 0):
    setup(x, y)
    if shape == "r":
        if rectangle_will_fit(x, y, l, h) is not False:
            t.fillcolor(color)
            t.begin_fill()
            t.forward(l)
            t.left(90)
            t.forward(h)
            t.left(90)
            t.forward(l)
            t.left(90)
            t.forward(h)
            t.setheading(0)
            t.end_fill()
            perimeter = 2 * (l + h)
            setup(0, 0)
            return perimeter
        else:
            return 0
    elif shape == 'c':
        if circle_will_fit(x, y, l) is not False:
            t.fillcolor(color)
            t.begin_fill()
            t.circle(l)
            t.end_fill()
            t.setheading(0)
            setup(0, 0)
            perimeter = PI * (l ^ 2)
            return perimeter
        else:
            return 0


def main():
    grid()
    p1 = draw_shape('r','red',100,100,70,50)
    p2 = draw_shape('c', 'green', -100, -100, 60)
    print(p1, p2)


main()



