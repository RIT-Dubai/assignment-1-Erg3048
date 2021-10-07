import turtle as t


XMAX = 200                #Defined constants as global variables
XMIN = -XMAX
YMAX = 200
YMIN = -YMAX
PI = 3.1415926535


def grid():               #Defined grid using max and min constants
    t.penup()
    t.goto(XMIN, YMAX)
    t.pendown()
    for i in range(4):
        t.forward(400)
        t.right(90)


def setup(x, y):           #defined turtle setup to use in most functions, simplifying the code
    t.penup()
    t.goto(x, y)
    t.pendown()


def rectangle_will_fit(x, y, l, h = 0):#Defined rectangle will fit to fit within the grid, without touching the border
    if (x+l >= XMAX or x <= XMIN):
        return False
    if (y+h >= YMAX or y <= YMIN):   #meant to be called in draw shape functions, wont continue if false
        return False


def circle_will_fit(x, y, r):        #same will fit function for circle
    if (x+r >= XMAX or x-r <= XMIN):
        return False
    if (y+r >= YMAX or y-r <= YMIN):
        return False


def triangle_will_fit(x, y, l):     #same will fit function for triangle
    if (x+l >= XMAX or x <= XMIN):
        return False
    h = l * 0.866   #root3/2 of the length gives height of equilateral triangle
    if (y+h >= YMAX or y <= YMIN):
        return False


def draw_shape(shape, color, x, y, l, h = 0): #draw shape function, indexed using if function
    setup(x, y)
    if shape == "r":
        if rectangle_will_fit(x, y, l, h) is not False: #nested if function to pass if the shape doesnt exceed the max and min variables
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
        else:   #if will fit functions return false, draw shape returns 0 to perimeter
            return 0
    elif shape == 'c':
        if circle_will_fit(x, y, l) is not False:
            t.fillcolor(color)
            t.begin_fill()
            t.circle(l)
            t.end_fill()
            t.setheading(0)
            setup(0, 0)
            perimeter = PI * l * 2
            return perimeter
        else:
            return 0
    elif shape == 't':
        if triangle_will_fit(x, y, l) is not False:
            t.fillcolor(color)
            t.begin_fill()
            t.forward(l)
            t.left(120)
            t.forward(l)
            t.left(120)
            t.forward(l)
            t.end_fill()
            t.setheading(0)
            setup(0, 0)
            perimeter = 3 * l
            return perimeter
        else:
            return 0
    return 0    # return 0 if no shape letter/incorrect shape letter is specified

def main():   #call to main for grid and all shapes
    grid()
    p1 = draw_shape('r','red',100,100,70,50)
    p2 = draw_shape('c', 'green', -100, -100, 60)
    p3 = draw_shape('t', 'blue', -100, 100, 80)
    print(p1, p2, p3) #returned perimeter to variables and printed them out


main() #calling main



