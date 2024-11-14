import math
import pytest
import circle
import square
import triangle
from calculate import calc


class TestCircle:
    def test_circle_area(self):
        assert circle.area(2) == math.pi * 2 * 2

    def test_circle_perimeter(self):
        assert circle.perimeter(2) == 2 * math.pi * 2


class TestSquare:
    def test_square_area(self):
        assert square.area(5) == 25
        assert square.area(2) == 4

    def test_square_perimeter(self):
        assert square.perimeter(4) == 16
        assert square.perimeter(2) == 8


class TestTriangle:
    def test_triangle_area(self):
        assert triangle.area(6, 6, 6) == 15.588457268119896
        assert triangle.area(8, 17, 15) == 60

    def test_triangle_perimeter(self):
        assert triangle.perimeter(6, 6, 6) == 18
        assert triangle.perimeter(8, 17, 15) == 40


class TestCalc:
    def test_not_positive_size(self):
        with pytest.raises(ValueError):
            calc("square", "perimeter", [-5])

    def test_correct_triangle_size(self):
        with pytest.raises(ValueError):
            calc("triangle", "perimeter", [-5, 5, 0])

    def test_correct_triangle_side_value(self):
        with pytest.raises(ValueError):
            calc("triangle", "perimeter", [3, 2, 5])

    def test_correct_fig(self):
        with pytest.raises(AssertionError):
            calc("tr", "perimeter", [6, 6, 6])

    def test_correct_func(self):
        with pytest.raises(AssertionError):
            calc("triangle", "per", [6, 6, 6])

    def test_correct_size(self):
        with pytest.raises(TypeError):
            calc("triangle", "perimeter", "triangle")
