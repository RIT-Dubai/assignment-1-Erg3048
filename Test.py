import turtle as t

import main


PI = 3.1415926535


def test_rectangle_will_fit():
    result = main.rectangle_will_fit(100, 100, 70, 50)
    assert result is not False, "Rectangle does not fit"


def test_draw_shape_rectangle():
    x = 0
    y = 0
    perimeter = main.draw_shape('r', 'red', 100, 100, 70, 50)
    assert t.fillcolor() == 'red', "color is incorrect"
    assert t.xcor() == x, "x coordinate is incorrect"
    assert t.ycor() == y, "y coordinate is incorrect"
    assert t.heading() == 0, "turtle not facing East"
    p = 2*(70+50)
    assert perimeter == p, "Perimeter is incorrect"


def test_circle_will_fit():
    result = main.circle_will_fit(-100, 100, 90)
    assert result is not False, "Circle does not fit"


def test_draw_shape_circle():
    x = 0
    y = 0
    perimeter = main.draw_shape('c','green', -100, -100, 80)
    assert t.fillcolor() == 'green', "color is incorrect"
    assert t.xcor() == x, "x coordinate is incorrect"
    assert t.ycor() == y, "y coordinate is incorrect"
    assert t.heading() == 0, "Turtle is not facing east"
    p = PI * 2 * 80
    assert perimeter == p, "Perimeter is incorrect"


def test_triangle_will_fit():
    result = main.triangle_will_fit(-100, 100, 80)
    assert result is not False, "Triangle does not fit"


def test_draw_shape_triangle():
    x = 0
    y = 0
    perimeter = main.draw_shape('t', 'blue', -100, 100, 80)
    assert t.fillcolor() == 'blue', "color is incorrect"
    assert t.xcor() == x, "x coordinate is incorrect"
    assert t.ycor() == y, "y coordinate is incorrect"
    assert t.heading() == 0, "Turtle is not heading East"
    p = 3 * 80
    assert perimeter == p, "Perimeter is incorrect"

