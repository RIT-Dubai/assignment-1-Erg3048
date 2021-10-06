import turtle as t

import main


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
    result = main.rectangle_will_fit(100, 100, 180)
    assert result is not False, "Circle does not fit"