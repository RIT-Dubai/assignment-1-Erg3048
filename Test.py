import turtle as t

import main


def test_rectangle_will_fit():
    result = main.rectangle_will_fit(100, 100, 70, 50)
    assert result is not False, "Rectangle does not fit"

